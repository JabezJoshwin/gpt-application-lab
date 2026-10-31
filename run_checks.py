"""Run each project's tests in isolation to avoid same-named module collisions."""
import subprocess,sys
from pathlib import Path
ROOT=Path(__file__).parent
failed=[]
for folder in ("BlogGenerator","EmailAssistant","RecommendationSystem","LegalAnalyzer","MedicalAssistant"):
    print("\n"+folder,flush=True)
    result=subprocess.run([sys.executable,"-m","unittest","discover","-s","tests","-v"],cwd=ROOT/folder)
    if result.returncode:failed.append(folder)
raise SystemExit(1 if failed else 0)
