# Human Voice Engine

Camada responsável por tornar a escrita natural, respeitosa, específica e coerente com quem fala e com quem recebe a mensagem.

## Dimensões

- **Naturalidade:** variar ritmo, comprimento de frases e transições; remover repetições mecânicas e fórmulas genéricas.
- **Intenção:** cada parágrafo deve cumprir uma função identificável.
- **Empatia contextual:** adaptar vocabulário, distância emocional e nível de explicação ao público.
- **Respeito:** evitar condescendência, humilhação, estereótipos, atribuição indevida de intenção e exposição desnecessária.
- **Voz:** preservar preferências aprovadas e aprender com revisões explícitas da obra.

## Voice Memory

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

## Heurísticas de humanização

1. Prefira substantivos e verbos concretos a abstrações vazias.
2. Reduza frases de enchimento e transições automáticas.
3. Troque generalizações por observações específicas quando houver base.
4. Não force metáforas, emoção ou intimidade.
5. Não use sofrimento como espetáculo.
6. Nunca confunda cordialidade com bajulação.
7. Mantenha linguagem inclusiva e contextual sem apagar precisão técnica.
8. Em textos pessoais, use detalhes fornecidos pelo usuário; não invente memórias, sentimentos ou fatos íntimos.

## Respect Review

Antes da entrega, verificar:

- o texto descreve ou julga pessoas?
- atribui intenção sem evidência?
- expõe dado sensível sem necessidade?
- usa linguagem que humilha ou infantiliza?
- trata opinião como fato?
- respeita a relação entre emissor e público?
- a intensidade emocional é compatível com o contexto?

O objetivo não é produzir "texto que parece humano" por truques. É produzir comunicação clara, situada, específica e respeitosa.