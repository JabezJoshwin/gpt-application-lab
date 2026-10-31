from utils import ModelError
def extract(client,text):
    result=client.generate("Extract explicitly reported symptoms and separately list symptoms explicitly denied. Preserve negation and uncertainty. Do not infer symptoms. Return JSON with reported and denied arrays of strings.",{"text":text},True)
    if not isinstance(result,dict) or any(not isinstance(result.get(k),list) or any(not isinstance(x,str) for x in result[k]) for k in ("reported","denied")):raise ModelError("Invalid symptom extraction")
    return result
