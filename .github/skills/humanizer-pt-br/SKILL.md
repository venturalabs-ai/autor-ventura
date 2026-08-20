---
name: humanizer-pt-br
description: Detect and remove AI-sounding patterns in Brazilian Portuguese text while preserving meaning tone and register. Use when finalizing or reviewing PT-BR copy drafts posts or chapters that must not read like generic AI output. Do not use when the text is already approved by a human editor or when the task is only factual verification without style review.
---

# Humanizer PT-BR

Ferramenta de revisão de estilo em português brasileiro. Varre o texto pelos 25 padrões abaixo e aplica regras de burstiness antes da entrega.

## Os 25 padrões

1. Exagero de significado — palavras maiores que o conteúdo sustenta.
2. Ênfase em notabilidade — "notável", "digno de nota", "impressionante" sem base.
3. Linguagem promocional — tom de vendas fora do contexto.
4. Gerúndio final de falsa profundidade — "levando a...", "proporcionando...".
5. Atribuição vaga — "especialistas afirmam", "estudos mostram" sem fonte.
6. Seção formulaica de desafios — "desafios e oportunidades" genérico.
7. Intervalos falsos — "entre 3 e 5 vezes" sem dado real.
8. Vocabulário de IA — "além disso", "crucial", "aprofundar", "no cenário atual", "é importante salientar", "cabe ressaltar", "sob essa ótica", "à luz de", "no que tange a".
9. Evasão de cópula — "serve como", "atua como" no lugar de verbos concretos.
10. Paralelismo negativo — "não apenas... mas também".
11. Regra dos três forçada — tríades decorativas sem função.
12. Rotação de sinônimos — trocar a mesma palavra por sinônimos só para variar.
13. Travessão em excesso — incisos encadeados.
14. Negrito em excesso — destaque sem critério.
15. Listas com subtítulo em negrito seguido de dois-pontos quando um parágrafo resolve.
16. Emojis decorativos — uso não funcional.
17. Title Case em headings — headings só com primeira palavra maiúscula em PT-BR.
18. Aspas curvas — usar aspas retas em PT-BR.
19. Ganchos dramáticos — "por que isso muda tudo?".
20. Rastros de chatbot — "espero ter ajudado", "claro!", "ótima pergunta".
21. Bajulação — elogio gratuito ao interlocutor.
22. Isenções de data de corte — "até a minha última atualização".
23. Conclusões genéricas — "o futuro parece promissor".
24. Frases de preenchimento — conteúdo zero que ocupa espaço.
25. Qualificação excessiva — camadas de "talvez", "potencialmente", "de certa forma".

## Regras de burstiness

- Alternar frases de 3–7 e 25–40 palavras.
- No máximo duas frases seguidas com a mesma extensão.
- Usar dois itens em vez de três quando a lista é fake.
- Variar o final dos parágrafos.

## Injeção de personalidade

Não basta remover o ruim. Adicionar voz, opinião, detalhe concreto e reconhecimento de complexidade. Preservar o significado e o tom do original.

## Rubrica /50

| Dimensão | Nota |
|---|---|
| Diretividade | /10 |
| Ritmo | /10 |
| Confiança no leitor | /10 |
| Autenticidade | /10 |
| Precisão | /10 |

Regra de bloqueio: texto com nota abaixo de 45 não é entregue. Refaça até passar.

## Pontos de verificação

- [ ] Os 25 padrões foram varridos
- [ ] Burstiness aplicado
- [ ] Nota maior ou igual a 45/50
- [ ] Significado e tom preservados
- [ ] Padrões banidos verbatim ausentes: "além disso", "é importante ressaltar", "no cenário atual", "vale destacar", "em conclusão", "não apenas... mas também", "espero ter ajudado", "claro!", "por que isso muda tudo?", "e é aqui que as coisas começam a fazer sentido", "e foi aí que tudo mudou"
