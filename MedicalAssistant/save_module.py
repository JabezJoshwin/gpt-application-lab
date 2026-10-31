from utils import save_report,sections
def save(report,path):
    if not report:raise ValueError("Analyze symptoms first")
    return save_report(sections(report),path)
