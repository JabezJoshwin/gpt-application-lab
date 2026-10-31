import argparse,json
from pathlib import Path
from datetime import datetime,timezone
from utils import Client,ModelError,save_report,sections
from input_module import collect,validate
from retrieval_module import load_history,retrieve
from intent_module import detect_intent
from reply_module import generate_reply
from tone_module import improve_tone
from summary_module import summarize
BASE=Path(__file__).parent
def run(client,customer,rows):
    intent=detect_intent(client,customer["email"]);history=retrieve(customer["email"],rows)
    return {"Date":datetime.now(timezone.utc).isoformat(),"Customer":customer,"Intent":intent,"Previous Interaction":history or "No similar interaction found","Generated Reply":generate_reply(client,customer,history,intent),"Summary":summarize(client,customer)}
def main():
    parser=argparse.ArgumentParser();parser.add_argument("--input",type=Path);parser.add_argument("--history",type=Path,default=BASE/"data/emails.csv");args=parser.parse_args();client=Client();rows=load_history(args.history)
    if args.input:
        report=run(client,validate(json.loads(args.input.read_text())),rows);print(sections(report));save_report(sections(report),BASE/"outputs/generated_reply.txt");return
    report={}
    while True:
        try:
            action=input("1 Enter email and generate reply | 2 Improve tone | 3 Summary | 4 Save | 5 Exit: ")
            if action=="5":break
            if action=="1":report=run(client,collect(),rows);print(sections(report))
            elif not report:raise ValueError("Enter an email first")
            elif action=="2":report["Generated Reply"]=improve_tone(client,report["Generated Reply"],input("Tone (Friendly/Formal/Empathetic): "));print(report["Generated Reply"])
            elif action=="3":print(report["Summary"])
            elif action=="4":print(save_report(sections(report),BASE/"outputs/generated_reply.txt"))
            else:print("Choose a listed action")
        except (ValueError,ModelError,OSError) as e: print("Error:",e)
if __name__=="__main__":
    try:main()
    except (ValueError,ModelError,OSError) as e:raise SystemExit(str(e))
