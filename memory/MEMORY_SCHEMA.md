# Memória Criativa Persistente — Esquema v2

A memória do Autor Ventura deve ser tratada como estado editorial explícito. O objetivo é preservar continuidade entre capítulos, sessões e agentes sem depender de lembrança implícita do modelo.

## Estrutura

```text
MEMORIA_ATIVA/
├── manifest.json
├── personagens/
│   ├── fichas.json
│   ├── relacionamentos.md
│   └── evolucao.md
├── mundo/
│   ├── geografia.md
│   ├── cronologia.md
│   ├── regras.md
│   └── glossario.md
├── enredo/
│   ├── arcos.md
│   ├── misterios.md
│   ├── cliffhangers.md
│   └── temas.md
├── estilo/
│   ├── tom.md
│   ├── ritmo.md
│   ├── pov.md
│   └── referencias.md
└── fatos/
    ├── validados.md
    ├── pendentes.md
    └── fontes.md
```

## manifest.json

Campos mínimos recomendados:

```json
{
  "work_id": "uuid",
  "title": "",
  "genre": "",
  "audience": "",
  "target_length": "",
  "status": "active",
  "current_chapter": 0,
  "current_scene": 0,
  "last_event": "",
  "last_emotional_state": "",
  "updated_at": "ISO-8601"
}
```

## Regras de atualização

- ler o estado antes de qualquer continuação;
- registrar mudança de personagem, cronologia, local, regra de mundo, conflito ou promessa narrativa;
- não apagar informação antiga silenciosamente: corrigir com registro explícito;
- separar fato real validado de decisão criativa;
- marcar dados ainda não checados como `PENDENTE`;
- ao trocar POV, tom ou timeline, registrar a alteração em `estilo/` e `mundo/cronologia.md`;
- manter mistérios, foreshadowing e cliffhangers até resolução explícita.

## Política de conflito

Quando dois registros entrarem em conflito:

1. preservar ambos temporariamente;
2. marcar o conflito;
3. escolher a versão canônica com base no texto publicado mais recente ou em decisão explícita do autor;
4. registrar a correção e seus impactos.

## Retomada de obra

Uma retomada deve produzir um pacote curto com:

- resumo de continuidade;
- personagens ativos e estado atual;
- conflitos e arcos abertos;
- mistérios e promessas pendentes;
- último evento confirmado;
- próximos pontos narrativos possíveis.

Essa memória é um protocolo de persistência editorial. A persistência real entre ambientes depende do sistema que armazenar estes arquivos ou registros.
