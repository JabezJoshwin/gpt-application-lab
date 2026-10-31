# Experiment 6: Educational medical symptom assistant

A modular, menu-driven Python application using OpenAI GPT-4. All input samples are demonstrations. The email history is converted from the instructor's supplied dataset.

## Run

Python 3.10 or later is required; the application uses only the Python standard library. No pip installation is necessary.

Set `OPENAI_API_KEY` in your shell using your own account configuration. Do not commit it. The default `OPENAI_MODEL` is `gpt-4`, as assigned; access and billing must be available in your account. These commands send the entered text to OpenAI. Use the supplied fictional sample for demonstrations.

From this directory:

```sh
python3 main.py
# Non-interactive complete pipeline with the sample input:
python3 main.py --input data/sample.json
# Offline unit and integration tests:
python3 -m unittest discover -s tests -v
```

The sample pipeline saves `outputs/medical_analysis.txt` after a successful model response. Interactive menus provide a separate save action. Runtime outputs are ignored by Git because they may contain user-provided data.

## Inputs and modules

Inputs: age, sex, symptoms, duration, severity, history, medications, allergies.

Pipeline: input_module → profile_module → symptom_module → context_module → prompt_module → analysis_module → question_module / safety_module → save_module.

Each module has one responsibility; `utils.py` contains the HTTP client, validation and atomic file writing. A model connection, authentication, truncation, or response-format error is reported explicitly. There is no simulated-response fallback in the application.

## Verification

Ten offline tests passed for this experiment on 31 October 2026. Tests use explicit test doubles for model calls. They verify application logic and HTTP request/error handling; they do not establish the quality of live model outputs. Live model verification and the Classroom screenshot evidence remain pending. See [verification](../docs/VERIFICATION.md).

## Notes

This prototype is for educational and informational use. It is not a diagnosis, a clinical triage system, or a replacement for a qualified healthcare professional. The disclaimer and general medical-attention message are application-controlled. Reported and denied symptoms are represented separately, but extraction accuracy and all generated health content still require careful evaluation. Avoid real patient data in demonstrations.
