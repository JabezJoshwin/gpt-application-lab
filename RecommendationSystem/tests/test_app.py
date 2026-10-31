import unittest
from ranking_module import rank
from profile_module import validate,analyze
from feedback_module import refine
from utils import ModelError
class Tests(unittest.TestCase):
    def test_ranking(self):
        items=[dict(name="A",reason="matches",score=60),dict(name="B",reason="matches",score=90)]
        self.assertEqual(rank({"recommendations":items},2)[0]["name"],"B")
    def test_reject_invalid_results(self):
        for result in [{}, {"recommendations":[]},{"recommendations":[dict(name="A",reason="ok",score=101)]},{"recommendations":[dict(name="A",reason="ok",score=True)]}]:
            with self.assertRaises(ModelError):rank(result,1)
    def test_duplicates(self):
        with self.assertRaises(ModelError):rank({"recommendations":[dict(name="A",reason="ok",score=1),dict(name="a",reason="ok",score=2)]},2)
    def test_feedback_reaches_model(self):
        class Fake:
            def generate(self,task,data,*args):
                self.data=data;return {"recommendations":[dict(name="AI practice",reason="fits feedback",score=80)]}
        fake=Fake();refine(fake,{"count":1},"No web development");self.assertEqual(fake.data["feedback"],"No web development")
    def test_empty_interests(self):
        with self.assertRaises(ValueError):validate(dict(name="A",age=20,background="CS",interests=" ",skill_level="beginner",preferred_category="course",goal="AI",count=1))
