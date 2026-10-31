import argparse
from pathlib import Path
from utils import Client,ModelError,sections,required
from input_module import read_document
from analysis_module import analyze
from preprocessing_module import preprocess,identify_sections
from save_module import save
BASE=Path(__file__).parent
def main():
    parser=argparse.ArgumentParser();parser.add_argument("--input",type=Path);args=parser.parse_args();client=Client("openai");text="";report={}
    if args.input:
        text=read_document(args.input);report=analyze(client,text);print(sections(report));save(report,BASE/"outputs/legal_analysis.txt");return
    while True:
        try:
            action=input("1 Load .txt | 2 Enter text | 3 Analyze | 4 Summary | 5 Save | 6 Exit: ")
            if action=="6":break
            if action in ("1","2"):
                text=read_document(input("Path: ")) if action=="1" else required(input("Legal text: "),"document");report={};print(preprocess(text));print("Sections:",len(identify_sections(text)))
            elif action=="3":report=analyze(client,text);print(sections(report))
            elif action=="4":print(report.get("Summary","Analyze a document first"))
            elif action=="5":
                if not report:raise ValueError("Analyze a document first")
                print(save(report,BASE/"outputs/legal_analysis.txt"))
            else:print("Choose a listed action")
        except (ValueError,ModelError,OSError) as e:print("Error:",e)
if __name__=="__main__":
    try:main()
    except (ValueError,ModelError,OSError) as e:raise SystemExit(str(e))
