import unittest,json
from pathlib import Path
from profile_module import validate
from analysis_module import analyze
from prompt_module import FIELDS
from safety_module import DISCLAIMER,guidance
from symptom_module import extract
from utils import ModelError
class Fake:
    def generate(self,task,data,*a):
        if "reported and denied" in task:return {"reported":["fever"],"denied":["breathing difficulty"]}
        return {k:"Insufficient information; ask a qualified professional." for k in FIELDS}
class Tests(unittest.TestCase):
    def profile(self):return validate(json.loads(Path("data/sample.json").read_text()))
    def test_report_always_has_disclaimer(self):
        report=analyze(Fake(),self.profile());self.assertEqual(report["Disclaimer"],DISCLAIMER);self.assertEqual(len(report),8)
    def test_negation_is_separate(self):self.assertEqual(analyze(Fake(),self.profile())["Reported Symptoms"]["denied"],["breathing difficulty"])
    def test_severe_guidance_without_model(self):
        profile=self.profile();profile["severity"]="severe";self.assertIn("reported severe",guidance(profile))
    def test_invalid_age(self):
        p=self.profile();p["age"]=-1
        with self.assertRaises(ValueError):validate(p)
    def test_bad_symptom_response(self):
        class Bad:
            def generate(self,*a):return {"reported":"fever","denied":[]}
        with self.assertRaises(ModelError):extract(Bad(),"fever")
