import unittest
from preprocessing_module import preprocess,chunk
from analysis_module import analyze
from prompt_module import FIELDS
from utils import ModelError
class Fake:
    def __init__(self):self.calls=[]
    def generate(self,task,data,*args):
        self.calls.append(data);return {f:"Not mentioned in the document." for f in FIELDS}
class Tests(unittest.TestCase):
    def test_normalization_preserves_legal_symbols(self):self.assertEqual(preprocess("  Payment:  ₹100\t due.\x00"),"Payment: ₹100 due.")
    def test_chunks_cover_entire_source(self):
        text="".join(chr(65+i%26) for i in range(15000));parts=chunk(text);self.assertEqual(parts[0],text[:6000]);self.assertEqual(parts[-1][-100:],text[-100:]);self.assertEqual(parts[0][-200:],parts[1][:200])
    def test_long_analysis_consolidates(self):
        fake=Fake();report=analyze(fake,"Contract clause. "*1000);self.assertGreater(len(fake.calls),2);self.assertIn("chunk_analyses",fake.calls[-1]);self.assertEqual(set(report),set(FIELDS))
    def test_blank_document(self):
        with self.assertRaises(ValueError):analyze(Fake()," ")
    def test_missing_fields(self):
        class Bad:
            def generate(self,*a):return {"Summary":"hi"}
        with self.assertRaises(ModelError):analyze(Bad(),"Contract")
