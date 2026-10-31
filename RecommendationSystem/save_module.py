from utils import save_report,sections
def save(profile,items,path):
    if not items:raise ValueError("Generate recommendations first")
    return save_report(sections({"Profile":profile,"Recommendations (subjective suitability scores)":items}),path)
