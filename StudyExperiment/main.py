"""Study experiment: the instructor sample uses qwen2.5:0.5b on Ollama."""
import os
from utils import Client,ModelError

def main():
    os.environ.setdefault("OLLAMA_MODEL","qwen2.5:0.5b")
    client=Client("ollama")
    print("Local Ollama study experiment. Type exit to finish.")
    while True:
        query=input("Ask something: ").strip()
        if query.lower()=="exit":break
        if not query:continue
        try:print(client.generate("You are a helpful assistant for e-commerce. Answer the user's query.",{"query":query}))
        except ModelError as exc:print("Error:",exc)
if __name__=="__main__":main()
