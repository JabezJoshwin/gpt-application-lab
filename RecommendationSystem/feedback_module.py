from recommendation_module import recommend
from utils import required
def refine(client,profile,feedback):return recommend(client,profile,required(feedback,"feedback"))
