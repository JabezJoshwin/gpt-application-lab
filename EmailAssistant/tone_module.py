def improve_tone(client,reply,tone):
    if tone not in ("Friendly","Formal","Empathetic"):raise ValueError("Choose Friendly, Formal or Empathetic")
    return client.generate("Rewrite the reply in the requested tone, preserving facts and uncertainty. Do not add commitments.",{"reply":reply,"tone":tone})
