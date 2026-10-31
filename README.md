# GPT application laboratory

Five modular Python implementations for the Building Applications using GPT-4 laboratory, experiments 2–6. Each experiment has an independent entry point, sample data, requirements file and tests.

| Experiment | Application | Assigned model | Code |
| --- | --- | --- | --- |
| 0 | Local LLM study application | Ollama / qwen2.5:0.5b | [StudyExperiment](StudyExperiment/) |
| 1 | E-commerce chatbot | Existing implementation | [Previously submitted repository](https://github.com/JabezJoshwin/E-commerce_chatbot) |
| 2 | Blog generator | Ollama / llama3.2 | [BlogGenerator](BlogGenerator/) |
| 3 | Email assistant | Ollama / llama3.2 | [EmailAssistant](EmailAssistant/) |
| 4 | Personalized recommendations | OpenAI GPT-4 | [RecommendationSystem](RecommendationSystem/) |
| 5 | Legal document analyzer | OpenAI GPT-4 | [LegalAnalyzer](LegalAnalyzer/) |
| 6 | Educational symptom assistant | OpenAI GPT-4 | [MedicalAssistant](MedicalAssistant/) |

## Quick start

Use Python 3.10+. Enter one experiment folder and run `python3 main.py`. Read that folder's README for model configuration and a non-interactive sample command. There are no pip dependencies.

Experiments 2–3 require a running Ollama service and `llama3.2`. Experiments 4–6 require an OpenAI API key with GPT-4 access. No key is bundled. The implementation does not silently replace the assigned model or create a fabricated model response.

## Verification

Run all 50 offline tests:

```sh
python3 run_checks.py
```

All 50 passed on 31 October 2026. Model calls in those tests use explicit test doubles. Live model execution, generated-output quality and Classroom screenshots are still unverified. See [verification details](docs/VERIFICATION.md) and [question mapping](docs/REQUIREMENTS.md).

The medical application is educational and informational only. It is not a diagnosis or a clinical triage system. The legal analyzer is an educational tool; review its output against the original document.

## Data and outputs

The email CSV contains 100 email/reply/intent records converted from the supplied classroom dataset. Customer and agent names were omitted. Other samples are fictional. Generated reports stay local under each `outputs/` directory and are ignored by Git.

[LinkedIn draft copy](linkedin/) describes the current verification state. No LinkedIn post has been published.

## API references

- [Ollama generate endpoint](https://docs.ollama.com/api/generate)
- [OpenAI GPT-4 model](https://developers.openai.com/api/docs/models/gpt-4)
- [OpenAI Chat Completions](https://developers.openai.com/api/reference/resources/chat/subresources/completions/methods/create)
