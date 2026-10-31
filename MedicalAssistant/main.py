import argparse,json
from pathlib import Path
from utils import Client,ModelError,sections,required
from input_module import collect
from profile_module import validate
from analysis_module import analyze
from question_module import questions
from safety_module import DISCLAIMER,guidance
from save_module import save
BASE=Path(__file__).parent
def main():
    parser=argparse.ArgumentParser();parser.add_argument("--input",type=Path);args=parser.parse_args();client=Client("openai");profile=None;report={};print(DISCLAIMER)
    if args.input:
        profile=validate(json.loads(args.input.read_text()));print(guidance(profile));report=analyze(client,profile);print(sections(report));save(report,BASE/"outputs/medical_analysis.txt");return
    while True:
        try:
            action=input("1 Patient information | 2 Symptoms | 3 Analyze | 4 Follow-up | 5 Possible conditions | 6 Guidance | 7 Disclaimer | 8 Save | 9 Exit: ")
            if action=="9":break
            if action=="7":print(DISCLAIMER);continue
            if action=="1":profile=collect();report={};print(guidance(profile));continue
            if not profile:raise ValueError("Enter patient information first")
            if action=="2":profile["symptoms"]=required(input("Symptoms: "),"symptoms");report={}
            elif action=="3":print(guidance(profile));report=analyze(client,profile);print(sections(report))
            elif action=="6":print(guidance(profile))
            elif not report:raise ValueError("Analyze symptoms first")
            elif action=="4":print(questions(report))
            elif action=="5":print(report["Possible Conditions"])
            elif action=="8":print(save(report,BASE/"outputs/medical_analysis.txt"))
            else:print("Choose a listed action")
        except (ValueError,ModelError,OSError) as e:print("Error:",e)
if __name__=="__main__":
    try:main()
    except (ValueError,ModelError,OSError) as e:raise SystemExit(str(e))
