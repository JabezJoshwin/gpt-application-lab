import unittest
from unittest.mock import patch
from input_module import validate
from main import run
from utils import Client,ModelError
from meta_module import generate_meta
class Fake:
    def generate(self,*args,**kwargs):
        if len(args)>2 and args[2]:return {"titles":["Title "+str(i) for i in range(5)]}
        return "Example educational text."
class Tests(unittest.TestCase):
    def test_complete_pipeline(self):
        report=run(Fake(),validate(dict(topic="AI",style="Professional",tone="Formal",word_count=500)))
        self.assertEqual(len(report),6);self.assertIn("Blog",report)
    def test_invalid_word_count(self):
        for count in [0,3001,"five",5.1,True]:
            with self.assertRaises(ValueError):validate(dict(topic="AI",style="P",tone="F",word_count=count))
    def test_blank_topic(self):
        with self.assertRaises(ValueError):validate(dict(topic=" ",style="P",tone="F",word_count=500))
    def test_meta_limit(self):
        class Long:
            def generate(self,*a):return "word "*100
        self.assertLessEqual(len(generate_meta(Long(),{})),160)
    def test_bad_intent(self):
        with patch.object(Client,"generate",return_value={"intent":"DELETE"}):
            with self.assertRaises(ModelError):Client().classify("delete",["SUMMARY"])
