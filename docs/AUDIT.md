# Auditoria de integridade — Autor Ventura

Data: 2026-08-20
Repositório: `venturalabs-ai/ventura.autor`
Método: comparação de claims do README/UPSTREAM/prompts com os artefatos reais do repositório; verificação externa do baseline upstream de personas; execução local da suíte de evals.

## Escopo

Este documento registra o que foi verificado e o que foi corrigido na auditoria de integridade do repositório. O foco é integridade documental e contratual (artefatos referenciados existem, números de proveniência batem, validações passam), não qualidade literária.

## Verificações executadas

| Verificação | Comando | Resultado |
|---|---|---|
| Evals de pipeline/proveniência/v2/v3 | `python scripts/run_evals.py` | PASS |
| Evals estruturais | `python evals/eval_structural.py` | PASS |
| Testes do roteador editorial | `python -m unittest discover -s editorial-evals -p 'test_*.py' -v` | 5/5 OK |
| Contrato das skills | `python scripts/validate_skills.py` | PASS (6 skills) |
| Lint | `ruff check scripts/ evals/ editorial-evals/` | PASS (0 violações) |
| Compilação Python | `python3 -m py_compile` | OK |
| Contagem de personas vs upstream `783f6a7` | `git` diff de árvore | 184 upstream + 3 BR = 187 |

## Achados corrigidos nesta auditoria

1. **Badge de licença com repositório antigo** — `README.md` apontava para `venturalabs-ai/autor-ventura` (nome antigo). Corrigido para `venturalabs-ai/ventura.autor`.
2. **Caminhos de personas inválidos nos agentes** — `02-arquiteto-narrativo.md` e `05-formatador.md` usavam caminhos no estilo Windows (`prompts\autor-ventura\personas\...`) que não existem no repositório. Corrigidos para `personas/agency-agents-pt-BR/<categoria>/`.
3. **Referências a skills inexistentes** — `04-humanizador.md` e `07-revisor-final.md` referenciam a skill `humanizer-pt-br` (com "25 padrões, checklist e pontuação") que não existia; `03-escritor-de-voz.md` e `07-revisor-final.md` referenciam a skill `language`. Adicionadas `.github/skills/humanizer-pt-br/SKILL.md` e `.github/skills/language/SKILL.md`, validando o contrato de skills.
4. **Referência a skill fantasma em `07-revisor-final.md`** — `revision-continuity`/`story-maintenance` não existem; a referência foi trocada pelo protocolo de continuidade real do repositório (`memory/MEMORY_SCHEMA.md` + registro de promessas do Arquiteto).
5. **Contagem de personas incorreta em `UPSTREAM.md`** — a tabela declarava 184 agentes (engineering 29, marketing 30) sem contabilizar 3 agentes BR já vendidos (engineering +1, marketing +2; total 187). Corrigido com verificação externa contra o upstream `msitarzewski/agency-agents@783f6a7` e enumeração dos agentes BR presentes.
6. **`voice_memory/` documentada como se existisse** — `voice-engine/README.md` e a skill `voice-memory` apresentavam a estrutura como convenção existente, mas o diretório não existe. A estrutura agora é qualificada como prevista e a skill referencia a documentação.
7. **Violações de lint** — imports desordenados (`editorial_router.py`, `run_evals.py`), `sys` não usado (`validate_skills.py`), shebang sem bit de execução (`score_semantic_outputs.py`, `validate_skills.py`). Corrigidos; `ruff check` agora passa e foi adicionado à CI.
8. **Documentação divergente** — árvore de `scripts/` no README listava 3 de 5 scripts; seção "Evals automáticos" omitia `validate_skills.py`. Corrigido.
9. **Ambiguidade de versão** — README diz "Autor Ventura v3.0" (versão do framework) enquanto `VERSION` = `0.1.0` (versão de release, usada pelas tags). Adicionada nota de esclarecimento no README.

## Observações (não corrigidas — recomendação)

- **Versões de ações do GitHub Actions flutuantes** — `ci.yml`, `release.yml` e `supply-chain.yml` usam tags maiores flutuantes (`actions/checkout@v4`, `actions/setup-python@v5`, `anchore/sbom-action@v0`, `softprops/action-gh-release@v2`). O workflow reutilizável `ventura-standard.yml` já é fixado por SHA. Recomenda-se fixar as demais ações por SHA de commit.
- **Sem arquivo de dependências Python** — o repositório não tem `requirements`/`pyproject.toml`. A CI instala `ruff` por versão explícita; recomenda-se adotar um lock mínimo se o conjunto de scripts crescer.
- **Cobertura dos `examples/` e `integrations/` do upstream** — o upstream `783f6a7` contém `examples/` e `integrations/` que não foram vendidos. A omissão é deliberada, mas o `UPSTREAM.md` não a declara; recomenda-se registrar a decisão.

## Limites da auditoria

- Os evals validam contratos estruturais e decisões de roteamento, não qualidade literária ou factual de saídas de modelo.
- A verificação de personas confirmou contagem e identidade dos arquivos contra o upstream; não revalidou a fidelidade da tradução agente a agente.
- As skills adicionadas (`humanizer-pt-br`, `language`) formalizam conteúdo que os agentes já exigiam; revisão humana de estilo continua necessária.
