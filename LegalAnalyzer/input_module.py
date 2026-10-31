from pathlib import Path
from utils import required
def read_document(path):
    path=Path(path)
    if path.suffix.lower()!=".txt":raise ValueError("Use a UTF-8 .txt file; PDF extraction is optional and not implemented")
    if path.stat().st_size>1000000:raise ValueError("Document exceeds 1 MB")
    return required(path.read_text(encoding="utf-8"),"document")
