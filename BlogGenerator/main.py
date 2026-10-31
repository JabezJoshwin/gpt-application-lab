"""Run: python3 main.py [--input data/sample.json]."""
import argparse,json
from pathlib import Path
from utils import Client,ModelError,save_report,sections
from input_module import collect,validate
from blog_module import generate_blog
from title_module import generate_titles
from summary_module import generate_summary
from keyword_module import generate_keywords
from meta_module import generate_meta
from intent_module import detect_intent
BASE=Path(__file__).parent
FUNCTIONS={"SUMMARY":generate_summary,"KEYWORD_GENERATION":generate_keywords,"META_DESCRIPTION":generate_meta,"TITLE_GENERATION":generate_titles}
def run(client,profile):
    blog=generate_blog(client,profile)
    report={"Profile":profile,"Blog":blog}
    for intent,fn in FUNCTIONS.items(): report[intent]=fn(client,{"blog":blog})
    return report
def main():
    parser=argparse.ArgumentParser();parser.add_argument("--input",type=Path);args=parser.parse_args();client=Client()
    if args.input:
        report=run(client,validate(json.loads(args.input.read_text())));print(sections(report));save_report(sections(report),BASE/"outputs/generated_blog.txt");return
    profile=None;blog=""
    while True:
        try:
            action=input("1 Profile | 2 Blog | 3 Titles | 4 Summary | 5 Keywords | 6 Meta | 7 Save | 8 Ask | 9 Exit: ").strip()
            if action=="9":break
            if action=="1":profile=collect();blog="";print(sections(profile));continue
            if action=="7":print(save_report(blog,BASE/"outputs/generated_blog.txt"));continue
            intent={"2":"BLOG_GENERATION","3":"TITLE_GENERATION","4":"SUMMARY","5":"KEYWORD_GENERATION","6":"META_DESCRIPTION"}.get(action)
            if action=="8": intent=detect_intent(client,input("Request: "))
            if intent=="EXIT":break
            if intent=="BLOG_GENERATION":
                profile=profile or collect();blog=generate_blog(client,profile);print(blog)
            elif intent in FUNCTIONS:
                if not blog:raise ValueError("Generate a blog first")
                print(FUNCTIONS[intent](client,{"blog":blog}))
            else:print("Choose a listed action")
        except (ValueError,ModelError,OSError) as e: print("Error:",e)
if __name__=="__main__":
    try: main()
    except (ValueError,ModelError,OSError) as e: raise SystemExit(str(e))
