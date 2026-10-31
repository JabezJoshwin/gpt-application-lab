from preprocessing_module import preprocess,chunk
from prompt_module import build_prompt,FIELDS
from utils import structured
def analyze(client,text):
    text=preprocess(text);parts=chunk(text)
    analyses=[structured(client.generate(build_prompt(),{"document_chunk":part,"chunk":i+1},True),FIELDS) for i,part in enumerate(parts)]
    if len(analyses)==1:return analyses[0]
    return structured(client.generate(build_prompt()+" Consolidate the chunk analyses. Deduplicate repeated clauses. Preserve conflicting terms and state uncertainty; absent in one chunk does not mean absent from the whole document.",{"chunk_analyses":analyses},True),FIELDS)
