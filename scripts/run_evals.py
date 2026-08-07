from pathlib import Path

PIPELINE = [
    '01-pesquisador.md',
    '02-arquiteto-narrativo.md',
    '03-escritor-de-voz.md',
    '04-humanizador.md',
    '05-formatador.md',
    '06-conector-emocional.md',
    '07-revisor-final.md',
]

failures = []
for filename in PIPELINE:
    path = Path(filename)
    if not path.exists():
        failures.append(f'missing pipeline stage: {filename}')
        continue
    text = path.read_text(encoding='utf-8')
    if len(text) < 1000:
        failures.append(f'{filename}: definition unexpectedly short')

persona_readme = Path('personas/agency-agents-pt-BR/README.md')
if not persona_readme.exists():
    failures.append('missing personas provenance README')
else:
    text = persona_readme.read_text(encoding='utf-8').lower()
    for marker in ['agency-agents', 'upstream', 'mit']:
        if marker not in text:
            failures.append(f'personas README missing provenance marker: {marker}')

if failures:
    print('AUTHOR EVALS: FAIL')
    for failure in failures:
        print(f'- {failure}')
    raise SystemExit(1)

print('AUTHOR EVALS: PASS (pipeline/provenance baseline)')
