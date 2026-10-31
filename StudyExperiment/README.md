# Study experiment: local LLM installation

This matches the instructor's Qwen sample using a standard-library HTTP client in place of the optional Ollama Python package.

```sh
ollama pull qwen2.5:0.5b
ollama serve
# In another terminal, from this folder:
python3 main.py
```

Ask an e-commerce question, then type `exit`. The default model is `qwen2.5:0.5b`; set OLLAMA_MODEL to override it explicitly.

The script compiles. A live run remains unverified because this execution session cannot connect to the local Ollama service. The Classroom installation assignment also requires an output screenshot and a YouTube link; neither is fabricated here.
