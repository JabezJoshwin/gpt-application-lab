import re,unicodedata
from utils import required
def preprocess(text):
    text=unicodedata.normalize("NFC",required(text,"document"))
    text="".join(c for c in text if c in "\n\t" or not unicodedata.category(c).startswith("C"))
    return "\n".join(re.sub(r"[ \t]+"," ",line).strip() for line in text.splitlines()).strip()
def identify_sections(text):return [p.strip() for p in re.split(r"\n\s*\n",text) if p.strip()]
def chunk(text,size=6000):
    # Lossless boundaries preserve all clauses; overlap supplies nearby context.
    if size<100:raise ValueError("Chunk size must be at least 100")
    return [text[i:i+size] for i in range(0,len(text),size-200 if size>200 else size)]
