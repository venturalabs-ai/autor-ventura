# Autor Ventura v2.0

[![License](https://img.shields.io/github/license/venturalabs-ai/autor-ventura)](LICENSE)

**Sistema editorial multiagente com memória criativa persistente, validação factual, adaptação por domínio e monitoramento de sinais de mercado.**

> Desenvolvido por **Ventura Labs AI** — Wemerson Mota de Oliveira

## O que mudou na v2.0

- memória criativa persistente estruturada por personagens, mundo, enredo, estilo e fatos;
- protocolo formal para iniciar, continuar e retomar obras após pausas;
- 10 domínios editoriais cobertos por regras específicas;
- framework para validação de fatos reais antes da publicação;
- guia de sinais de mercado para romantasy, thriller, devocional, literatura nacional, mangá e clássicos revividos;
- utilitário Python para inicializar e validar a memória de uma obra;
- system prompt consolidado em `prompts/autor-ventura-v2.md`.

## Pipeline editorial

**Pesquisa → Arquitetura → Escrita → Humanização → Formatação → Conexão emocional → Revisão final → Atualização de memória**

## Especialistas

```text
autor-ventura/
├── 01-pesquisador.md
├── 02-arquiteto-narrativo.md
├── 03-escritor-de-voz.md
├── 04-humanizador.md
├── 05-formatador.md
├── 06-conector-emocional.md
├── 07-revisor-final.md
├── prompts/
│   └── autor-ventura-v2.md
├── memory/
│   └── MEMORY_SCHEMA.md
├── docs/
│   └── MARKET_SIGNALS.md
├── scripts/
│   ├── run_evals.py
│   └── memory_manager.py
└── personas/
    └── agency-agents-pt-BR/
```

## Memória Criativa Persistente

O Autor Ventura não depende apenas do contexto implícito da IA. A continuidade é tratada como um estado editorial explícito:

```text
MEMORIA_ATIVA/
├── personagens/
├── mundo/
├── enredo/
├── estilo/
└── fatos/
```

O esquema completo está em [`memory/MEMORY_SCHEMA.md`](memory/MEMORY_SCHEMA.md).

### Inicializar memória de uma nova obra

```bash
python scripts/memory_manager.py init memoria/minha-obra \
  --title "Minha obra" \
  --genre "thriller psicológico" \
  --audience "adulto" \
  --target-length "80.000 palavras"
```

### Validar a estrutura

```bash
python scripts/memory_manager.py validate memoria/minha-obra
```

## 10 domínios de escrita

1. literatura infantil;
2. livros técnicos;
3. ficção comercial / best-seller;
4. esportes;
5. sentimentos e psicologia narrativa;
6. fatos e documentário;
7. cultura pop, música e cinema;
8. ciência e divulgação científica;
9. história e biografia;
10. humor e sátira.

Cada domínio possui regras próprias de tom, estrutura, validação e continuidade no system prompt v2.

## Validação factual

Sempre que um texto tocar o mundo real de forma verificável, o fluxo deve separar:

**fato confirmado → interpretação → hipótese → decisão criativa**.

Não devem ser inventadas estatísticas, citações de pessoas reais, datas, dados técnicos, placares, recordes, regras oficiais ou fontes bibliográficas.

## Inteligência de mercado

`docs/MARKET_SIGNALS.md` mantém um framework para observar sinais editoriais sem transformar tendências em fórmulas de escrita. Qualquer alegação sobre rankings, vendas, Nielsen/BookScan, PublishNews, NYT ou outras listas deve ser validada e datada antes de uso comercial.

## Como usar o system prompt

O prompt consolidado está em:

```text
prompts/autor-ventura-v2.md
```

Ele pode ser usado como base de configuração em sistemas de agentes compatíveis. A persistência real entre sessões depende de o ambiente salvar e recarregar o estado definido em `memory/`.

## Casos de uso

- romances e séries com continuidade longa;
- livros técnicos e profissionais;
- literatura infantil;
- biografias e documentários;
- conteúdo esportivo;
- divulgação científica;
- roteiros e projetos editoriais;
- produção de long-form com rastreabilidade factual.

## Princípios

- responsabilidades separadas por especialista;
- memória explícita, não apenas contexto implícito;
- continuidade entre capítulos e sessões;
- revisão antes da entrega;
- validação de fatos reais;
- voz adaptada ao gênero e ao público;
- mercado orienta posicionamento, não substitui originalidade;
- nenhum agente substitui revisão humana em conteúdo jurídico, médico, financeiro ou regulatório.

## Status

Biblioteca de prompts, regras, personas e utilitários para workflows editoriais multiagentes. A presença de memória estruturada melhora rastreabilidade, mas não cria persistência automática em qualquer modelo: o sistema hospedeiro precisa armazenar e recarregar o estado.

## Licença

MIT — consulte [LICENSE](LICENSE).

## Autor

Wemerson Mota de Oliveira — Ventura Labs AI

[GitHub](https://github.com/venturalabs-ai) · [LinkedIn](https://www.linkedin.com/in/wemerson-mota-de-oliveira-81aa8226/)
