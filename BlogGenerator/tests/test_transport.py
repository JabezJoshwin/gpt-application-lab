import unittest,json
from unittest.mock import patch
from io import BytesIO
from utils import Client,ModelError,save_report
from urllib.error import URLError
from pathlib import Path
import tempfile
class Tests(unittest.TestCase):
    def test_network_error_is_explicit(self):
        with patch("utils.urlopen",side_effect=URLError("offline")):
            with self.assertRaises(ModelError):Client().generate("task",{})
    def test_no_api_key(self):
        with patch.dict("os.environ",{},clear=True):
            with self.assertRaises(ModelError):Client("openai").generate("task",{})
    def test_ollama_request(self):
        with patch("utils.urlopen",return_value=BytesIO(json.dumps({"response":"ok","done":True}).encode())) as call:
            self.assertEqual(Client().generate("task",{}),"ok");req=call.call_args.args[0];body=json.loads(req.data);self.assertFalse(body["stream"])
    def test_json_and_truncation(self):
        with patch("utils.urlopen",return_value=BytesIO(json.dumps({"response":"{bad}","done":True}).encode())):
            with self.assertRaises(ModelError):Client().generate("task",{},True)
        with patch.dict("os.environ",{"OPENAI_API_KEY":"test-only"}),patch("utils.urlopen",return_value=BytesIO(json.dumps({"choices":[{"finish_reason":"length","message":{"content":"partial"}}]}).encode())):
            with self.assertRaises(ModelError):Client("openai").generate("task",{})
    def test_atomic_save_and_no_blank(self):
        with tempfile.TemporaryDirectory() as directory:
            path=Path(directory)/"nested/report.txt";save_report("ok",path);self.assertEqual(path.read_text(),"ok")
            with self.assertRaises(ValueError):save_report("",path)
            self.assertEqual(path.read_text(),"ok")
