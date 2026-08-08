# Security Policy

## Reporting

Report vulnerabilities privately via GitHub Security Advisories or email Tec.Wemerson@outlook.com.

Do not open public issues for secrets, credential leaks, or exploitable flaws.

## Scope

This repository is primarily an **editorial agent pack** (prompts, skills, evals). It does not ship a production runtime by default.

## Rules

- Never commit API keys, tokens, private keys, or `.env` files with secrets
- Never invent sources, DOIs, interviews, or confidence signals in claim ledgers
- Marketing-style absolute safety claims are rejected by the repository-safety CI gate
- Shared security baseline is pinned in `.github/workflows/ventura-standard.yml`

## Response

Acknowledged reports should receive an initial response within 7 days when contact details are valid.
