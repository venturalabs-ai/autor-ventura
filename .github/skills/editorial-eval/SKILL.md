---
name: editorial-eval
description: Add or run Autor Ventura structural editorial evals for routing publication packs voice and factual gates. Use when changing prompts router logic memory behavior or review constraints. Do not use when judging literary quality from one generated draft without a defined test contract.
---

# Editorial eval

- Reproduce the changed behavior with a focused case before modifying tests.
- Use the existing runners under `scripts/` `evals/` and `editorial-evals/`.
- Test routing structure required gates and prohibited fabrication separately.
- Add boundary cases for missing evidence privacy limits or mismatched medium.
- Keep fixtures synthetic unless approved source material is required.
- Run `python scripts/run_evals.py` and the repository's documented eval commands.
- Treat passing structural evals as regression evidence not proof of factual or literary quality.
