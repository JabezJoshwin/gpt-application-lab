# Verification on 31 October 2026

| Check | Result |
| --- | --- |
| Compilation of experiments 2–6 | Passed |
| Experiment 2 offline tests | 10 passed |
| Experiment 3 offline tests | 10 passed |
| Experiment 4 offline tests | 10 passed |
| Experiment 5 offline tests | 10 passed |
| Experiment 6 offline tests | 10 passed |
| Email CSV conversion | 100 rows; email, reply and intent retained |
| Ollama connection | Blocked: this execution session cannot connect to localhost:11434 |
| GPT-4 execution | Not run: no API key configured for this work |
| Live response quality | Not evaluated |
| Classroom screenshot evidence | Pending live execution |

Tests use simulated model responses to check complete application pipelines, data validation, retrieval relevance, ranking, feedback propagation, chunk coverage, mandatory disclaimers and network/response-format failures. They are not evidence of model accuracy or a successful live model demonstration.

Re-run `python3 run_checks.py` from the root. Live verification commands are in each experiment's README. Review actual outputs before using them in a record or a public demonstration.
