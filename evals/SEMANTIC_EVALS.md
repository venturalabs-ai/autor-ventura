# Semantic evals

These rubrics score externally generated outputs. They do not call a model and do not prove Autor Ventura quality by themselves.

Run:

```bash
python scripts/score_semantic_outputs.py --outputs reports/model-output.jsonl
```

A publishable report must include model/provider/version, configuration, date, repository commit, the exact cases and the exact generated outputs. Manual fixtures may test the scorer only and must not be reported as model performance.
