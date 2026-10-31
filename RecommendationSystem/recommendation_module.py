from prompt_module import build_prompt
from ranking_module import rank
def recommend(client,profile,feedback=""):
    return rank(client.generate(build_prompt(profile["count"]),{"profile":profile,"feedback":feedback},True),profile["count"])
