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

V2_REQUIRED = [
    'prompts/autor-ventura-v2.md',
    'memory/MEMORY_SCHEMA.md',
    'docs/MARKET_SIGNALS.md',
    'scripts/memory_manager.py',
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

for filename in V2_REQUIRED:
    path = Path(filename)
    if not path.exists():
        failures.append(f'missing v2 artifact: {filename}')
        continue
    if len(path.read_text(encoding='utf-8')) < 300:
        failures.append(f'{filename}: v2 artifact unexpectedly short')

prompt_path = Path('prompts/autor-ventura-v2.md')
if prompt_path.exists():
    prompt = prompt_path.read_text(encoding='utf-8').lower()
    for marker in [
        'memória criativa persistente',
        'literatura infantil',
        'livros técnicos',
        'esportes',
        'sentimentos',
        'documentário',
        'cultura pop',
        'ciência',
        'história',
        'humor',
        'validação factual',
    ]:
        if marker not in prompt:
            failures.append(f'v2 prompt missing marker: {marker}')

memory_schema = Path('memory/MEMORY_SCHEMA.md')
if memory_schema.exists():
    schema = memory_schema.read_text(encoding='utf-8').lower()
    for marker in ['personagens', 'mundo', 'enredo', 'estilo', 'fatos', 'manifest.json']:
        if marker not in schema:
            failures.append(f'memory schema missing section: {marker}')

market = Path('docs/MARKET_SIGNALS.md')
if market.exists():
    market_text = market.read_text(encoding='utf-8').lower()
    for marker in ['romantasy', 'thriller', 'devocional', 'literatura nacional', 'mangá', 'clássicos']:
        if marker not in market_text:
            failures.append(f'market framework missing category: {marker}')
    if 'validar' not in market_text:
        failures.append('market framework must require current validation')

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

print('AUTHOR EVALS: PASS (pipeline/provenance/v2 memory baseline)')
