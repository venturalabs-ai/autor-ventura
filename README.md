# Autor Ventura v3.0

[![License](https://img.shields.io/github/license/venturalabs-ai/autor-ventura)](LICENSE)

**Sistema editorial multiagente que decide como escrever antes de escrever: quem fala, para quem, por quê, em qual meio, com quais evidências, com qual emoção e dentro de quais limites.**

> Ventura Labs AI — Wemerson Mota de Oliveira

## O salto da v3

A v2 estruturou memória criativa, continuidade, domínios e validação factual. A v3 adiciona uma camada de **inteligência editorial por contexto de publicação**.

O sistema agora separa:

**speaker → audience → purpose → medium → evidence → emotion → limits**

antes de selecionar estrutura, voz e critérios de revisão.

## Arquitetura

```text
PEDIDO
   ↓
EDITORIAL ROUTER
   ↓
AUDIENCE + PURPOSE MODEL
   ↓
PUBLICATION PACK
   ↓
RESEARCH / FACT ENGINE
   ↓
MEMORY ENGINE
   ↓
STRUCTURE ARCHITECT
   ↓
DRAFT
   ↓
HUMAN VOICE ENGINE
   ↓
RESPECT & SENSITIVITY REVIEW
   ↓
DOMAIN REVIEW
   ↓
FACT / CITATION CHECK
   ↓
EDITOR DE VERDADE
   ↓
FORMAT VALIDATOR
   ↓
FINAL
```

## Novos módulos v3

```text
autor-ventura/
├── publication-packs/
│   ├── README.md
│   ├── editais.md
│   ├── magazine.md
│   └── symposium.md
├── voice-engine/
│   └── README.md
├── academic/
│   └── README.md
├── journalism/
│   └── README.md
├── broadcast/
│   └── README.md
├── ceremonial/
│   └── README.md
├── editorial-evals/
│   ├── README.md
│   └── test_editorial_router.py
├── prompts/
│   ├── autor-ventura-v2.md
│   └── autor-ventura-v3.md
└── scripts/
    ├── editorial_router.py
    ├── memory_manager.py
    └── run_evals.py
```

## Publication Packs

A mesma informação recebe tratamento diferente conforme o meio:

| Meio | Prioridade editorial |
|---|---|
| Jornal | lead, 5W1H, atribuição, contexto e Claim Ledger |
| TV / rádio / vídeo | texto falado, duração, OFF, sonora, passagem e GC |
| Revista / long-form | cena, nut graf, contexto, profundidade e precisão |
| Livro | continuidade longa, voz, arco, memória e coerência |
| Edital | requisito, evidência, documento, resposta e risco |
| Acadêmico | pergunta, método, evidência, discussão, limitações e integridade |
| Simpósio | consistência entre abstract, paper, pôster, slides e fala |
| Cerimonial | memória real, significado, privacidade, autenticidade e promessa |

## Human Voice Engine

Humanização não é esconder o uso de IA. É produzir comunicação natural, específica e respeitosa.

O motor trabalha:

- intenção por parágrafo;
- ritmo e variação de frase;
- formalidade adequada ao público;
- vocabulário preferido;
- exemplos aprovados e rejeitados;
- emoção proporcional ao contexto;
- redução de clichês, redundâncias e transições automáticas;
- respeito, privacidade e ausência de memórias inventadas sobre pessoas reais.

## Memória de voz

Além da memória criativa v2, a v3 prevê:

```text
voice_memory/
├── author_profile.json
├── audience_profile.json
├── preferred_vocabulary.json
├── avoid_list.json
├── formality.json
├── approved_samples/
├── rejected_samples/
├── rhythm.json
└── revision_history.json
```

## Roteador editorial executável

```bash
python scripts/editorial_router.py \
  --speaker "repórter" \
  --audience "público geral" \
  --purpose "informar" \
  --medium "jornal" \
  --limit "não publicar nomes de menores"
```

O retorno informa pack, nível de evidência, emoção e verificações obrigatórias.

## Jornalismo

O Journalism Pack exige separação entre fato, alegação, análise e opinião, atribuição de informação contestável, verificação de nomes e números e coerência entre manchete e corpo.

Afirmações verificáveis relevantes podem ser registradas em um **Claim Ledger** com fonte, data e nível de confiança.

## TV, rádio e vídeo

O Broadcast Pack escreve para o ouvido: frases pronunciáveis, uma ideia principal por frase, adaptação de números e siglas, estrutura de roteiro e estimativa operacional de duração.

## Acadêmico

O Academic Pack atende monografias, TCCs, dissertações, teses, artigos e projetos de pesquisa como **copiloto de redação e coerência**.

Não deve inventar DOI, referência, participante, entrevista, amostra, dado, resultado ou aprovação ética. O Coherence Gate verifica alinhamento entre pergunta, objetivo, método, resultados, discussão e conclusão.

## Editais

O sistema converte exigências em matriz:

**requisito → evidência → documento comprobatório → resposta → risco**

Um item nunca é marcado como atendido sem evidência.

## Votos, homenagens e cerimônias

O Ceremonial Pack prioriza material humano real. Memórias, sentimentos, falas e acontecimentos não são inventados. O sistema busca especificidade, privacidade, consentimento e promessas plausíveis.

## Editor de Verdade

A última revisão procura:

- frases dispensáveis;
- clichês e exageros;
- repetição;
- sentimentalismo artificial;
- argumentos fracos;
- fatos sem fonte;
- palavras difíceis sem necessidade;
- conclusões maiores que as evidências;
- mudança involuntária de voz.

## Evals automáticos

A CI executa:

```bash
python scripts/run_evals.py
python evals/eval_structural.py
python -m unittest discover -s editorial-evals -p 'test_*.py' -v
```

Os testes cobrem roteamento e gates para jornalismo, broadcast, acadêmico, edital, cerimonial e voz. Esses evals reduzem falhas previsíveis, mas não provam qualidade literária ou factual por si só.

## Compatibilidade com v2

A v3 preserva:

- Memória Criativa Persistente;
- 10 domínios de escrita;
- validação factual;
- sinais de mercado;
- pipeline de sete especialistas;
- utilitário de memória;
- provenance e security gates existentes.

## System prompt

Use:

```text
prompts/autor-ventura-v3.md
```

## Princípios

- meio e audiência mudam a escrita;
- benefício editorial vem antes de ornamentação;
- fatos reais exigem rastreabilidade compatível com o risco;
- emoção deve ser proporcional e verdadeira ao material fornecido;
- respeito não é opcional;
- nenhuma fonte, memória, citação ou resultado deve ser inventado;
- revisão humana continua necessária em conteúdo de alto impacto.

## Status

Framework editorial multiagente com roteamento executável, prompts, memória e evals estruturais. A qualidade final depende do modelo, das fontes, do contexto fornecido e da revisão aplicada.

## Licença

MIT — consulte [LICENSE](LICENSE).
