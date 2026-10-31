import argparse,json
from pathlib import Path
from utils import Client,ModelError,sections
from input_module import collect
from profile_module import validate,analyze
from recommendation_module import recommend
from feedback_module import refine
from explanation_module import explain
from intent_module import detect_intent
from save_module import save
BASE=Path(__file__).parent
def main():
    parser=argparse.ArgumentParser();parser.add_argument("--input",type=Path);args=parser.parse_args();client=Client("openai");profile=None;items=[];feedback=[]
    if args.input:
        profile=validate(json.loads(args.input.read_text()));items=recommend(client,profile);print(sections({"Profile":profile,"Preference Analysis":analyze(profile),"Ranked Recommendations":items}));save(profile,items,BASE/"outputs/recommendations.txt");return
    while True:
        try:
            action=input("1 Profile | 2 Recommend | 3 Refine | 4 Explain | 5 Save | 6 Ask | 7 Exit: ");intent={"1":"SHOW_PROFILE","2":"GENERATE_RECOMMENDATION","3":"REFINE_RECOMMENDATION","4":"EXPLAIN_RECOMMENDATION","5":"SAVE_RECOMMENDATION","7":"EXIT"}.get(action);request=""
            if action=="6":request=input("Request: ");intent=detect_intent(client,request)
            if intent=="EXIT":break
            if intent=="SHOW_PROFILE":
                profile=profile or collect();print(sections({"Profile":profile,"Preference Analysis":analyze(profile)}))
            elif intent=="GENERATE_RECOMMENDATION":profile=profile or collect();items=recommend(client,profile);print(sections({"Ranked Recommendations":items}))
            elif intent=="REFINE_RECOMMENDATION":
                if not items:raise ValueError("Generate recommendations first")
                feedback.append(request or input("Feedback: "));items=refine(client,profile,"\n".join(feedback));print(sections({"Refined Recommendations":items}))
            elif intent=="EXPLAIN_RECOMMENDATION":print(explain(items) if items else "Generate recommendations first")
            elif intent=="SAVE_RECOMMENDATION":print(save(profile,items,BASE/"outputs/recommendations.txt"))
            else:print("Choose a listed action")
        except (ValueError,ModelError,OSError) as e:print("Error:",e)
if __name__=="__main__":
    try:main()
    except (ValueError,ModelError,OSError) as e:raise SystemExit(str(e))
