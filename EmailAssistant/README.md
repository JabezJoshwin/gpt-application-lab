# Experiment 3: Intelligent email assistant

A modular, menu-driven Python application using Ollama with llama3.2. All input samples are demonstrations. The email history is converted from the instructor's supplied dataset.

## Run

Python 3.10 or later is required; the application uses only the Python standard library. No pip installation is necessary.

Start Ollama and install the assigned model:

```sh
ollama serve
# In a second terminal:
ollama pull llama3.2
```

From this directory:

```sh
python3 main.py
# Non-interactive complete pipeline with the sample input:
python3 main.py --input data/sample.json
# Offline unit and integration tests:
python3 -m unittest discover -s tests -v
```

The sample pipeline saves `outputs/generated_reply.txt` after a successful model response. Interactive menus provide a separate save action. Runtime outputs are ignored by Git because they may contain user-provided data.

## Inputs and modules

Inputs: customer name, subject, customer email.

Pipeline: input_module → intent_module → retrieval_module → reply_module → tone_module / summary_module → utils.save_report.

Each module has one responsibility; `utils.py` contains the HTTP client, validation and atomic file writing. A model connection, authentication, truncation, or response-format error is reported explicitly. There is no simulated-response fallback in the application.

## Verification

Ten offline tests passed for this experiment on 31 October 2026. Tests use explicit test doubles for model calls. They verify application logic and HTTP request/error handling; they do not establish the quality of live model outputs. Live model verification and the Classroom screenshot evidence remain pending. See [verification](../docs/VERIFICATION.md).

## Notes

Retrieval uses local TF-IDF-weighted cosine similarity, not sentence embeddings. The 100-row CSV has email, reply and intent columns; customer names and agent names were omitted. Historical replies are context examples, not evidence of completed actions for a new customer. Replies are saved locally and are never sent.
