import unittest
from pathlib import Path
from main import run
from retrieval_module import retrieve,load_history
from tone_module import improve_tone
from utils import Client,ModelError
from unittest.mock import patch
class Fake:
    def classify(self,*a):return "Delivery Issue"
    def generate(self,*a):return "Please share your order reference so we can investigate."
class Tests(unittest.TestCase):
    def test_dataset(self):
        rows=load_history(Path("data/emails.csv"));self.assertEqual(len(rows),100);self.assertTrue(all(r["email"] and r["reply"] for r in rows))
    def test_relevant_retrieval(self):
        rows=[{"email":"shipment delivery delayed","reply":"A"},{"email":"refund payment money","reply":"B"}]
        self.assertEqual(retrieve("delivery delayed",rows)["reply"],"A")
    def test_no_match(self):self.assertIsNone(retrieve("xyz",[{"email":"refund","reply":"A"}]))
    def test_pipeline(self):
        report=run(Fake(),{"customer_name":"Test","subject":"Delay","email":"Delivery delayed"},[{"email":"Delivery delayed","reply":"Historical reply"}]);self.assertIn("Date",report);self.assertEqual(report["Intent"],"Delivery Issue")
    def test_invalid_tone(self):
        with self.assertRaises(ValueError):improve_tone(Fake(),"hello","angry")
