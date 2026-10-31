# Mapping to the supplied lab questions

| Experiment | Questions | Implementation |
| --- | --- | --- |
| 2 | Q1–Q2 inputs and display | input_module.py, main.py |
| 2 | Q3–Q4 prompt and blog | blog_module.py, utils.Client |
| 2 | Q5 five titles | title_module.py |
| 2 | Q6 keywords | keyword_module.py |
| 2 | Q7 summary | summary_module.py |
| 2 | Q8 meta description | meta_module.py |
| 2 | Q10 intent routing | intent_module.py |
| 2 | Q11 continuous application and saving | main.py, utils.save_report |
| 3 | Q1–Q2 customer input and display | input_module.py, main.py |
| 3 | Q3 intent | intent_module.py |
| 3 | Q4–Q5 CSV and retrieval | data/emails.csv, retrieval_module.py |
| 3 | Q6 replies | reply_module.py |
| 3 | Q7 tone | tone_module.py |
| 3 | Q8 summary | summary_module.py |
| 3 | Q9 date/email/reply/intent saving | main.py, utils.save_report |
| 3 | Q10 continuous application | main.py |
| 4 | Q1–Q3 profile and analysis | input_module.py, profile_module.py |
| 4 | Q4 prompt | prompt_module.py |
| 4 | Q5–Q7 generate/rank/explain | recommendation_module.py, ranking_module.py, explanation_module.py |
| 4 | Q8 feedback | feedback_module.py |
| 4 | Q9 intent | intent_module.py |
| 4 | Q10 continuous application and saving | main.py, save_module.py |
| 5 | Q1–Q2 text and file input | input_module.py, main.py |
| 5 | Q3 normalize/sections/chunks | preprocessing_module.py |
| 5 | Q4 constrained prompt | prompt_module.py |
| 5 | Q5 structured analysis and summary | analysis_module.py |
| 5 | Q6 save | save_module.py |
| 5 | Q7 application | main.py |
| 6 | Q1 patient context | input_module.py, profile_module.py |
| 6 | Q2 symptom extraction | symptom_module.py |
| 6 | Q3 missing information | context_module.py |
| 6 | Q4 prompt | prompt_module.py |
| 6 | Q5–Q6 possibilities and follow-up | analysis_module.py, question_module.py |
| 6 | Q7 attention guidance | safety_module.py |
| 6 | Q8 structured report | analysis_module.py |
| 6 | Q9 disclaimer | safety_module.py |
| 6 | Q10 save | save_module.py |
| 6 | Q11 integrated application | main.py |

The experiment 2 question sheet skips Q9; numbering above follows the source. The experiment 6 preparation PDF is internally mislabeled Experiment 5; its Classroom topic, medical question sheet and record template identify it as Experiment 6.

Optional PDF extraction for the legal analyzer was not implemented. Email retrieval uses a dependency-free TF-IDF baseline rather than Sentence Transformers. Recommender preference analysis is part of profile_module.py. Save helpers for the blog and email applications live in utils.py. These choices preserve the required behaviors with fewer runtime dependencies.
