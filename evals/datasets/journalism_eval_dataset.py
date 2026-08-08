"""
Dataset de Evals Semânticos - Jornalismo
Autor Ventura v3.0

50 casos de teste para validar qualidade de escrita jornalística.
Cada caso inclui: brief, output esperado, e critérios de avaliação.
"""

JOURNALISM_EVAL_CASES = [
    {
        "id": "jrn_001",
        "brief": {
            "speaker": "Repórter",
            "audience": "Público geral",
            "purpose": "Informar sobre nova lei",
            "medium": "Notícia online",
            "evidence": "Alto",
            "emotion": "Neutro",
            "context": "Nova lei de proteção de dados aprovada no Senado"
        },
        "expected_qualities": [
            "Lead com 5W1H completo",
            "Atribuição clara de todas afirmações",
            "Distinção entre fato e opinião",
            "Contexto legislativo relevante",
            "Contrapontos quando aplicável",
            "Título sustentado pelo corpo",
            "Claim Ledger para dados verificáveis"
        ],
        "negative_patterns": [
            "Opinião não atribuída",
            "Lead enterrado",
            "Título clickbait não sustentado",
            "Falta de contexto",
            "Confusão fato/opinião"
        ],
        "target_word_count": "300-500"
    },
    {
        "id": "jrn_002",
        "brief": {
            "speaker": "Jornalista de tecnologia",
            "audience": "Leitores interessados em tech",
            "purpose": "Explicar nova funcionalidade de IA",
            "medium": "Matéria de tecnologia",
            "evidence": "Alto",
            "emotion": "Neutro com leve entusiasmo",
            "context": "OpenAI lança GPT-5 com capacidades multimodais avançadas"
        },
        "expected_qualities": [
            "Explicação técnica acessível",
            "Comparação com versões anteriores",
            "Citações de especialistas",
            "Implicações práticas claras",
            "Limitações mencionadas",
            "Fontes técnicas verificáveis"
        ],
        "negative_patterns": [
            "Jargão excessivo sem explicação",
            "Hype não fundamentado",
            "Comparações imprecisas",
            "Omissão de limitações"
        ],
        "target_word_count": "600-800"
    },
    {
        "id": "jrn_003",
        "brief": {
            "speaker": "Repórter de economia",
            "audience": "Investidores e público geral",
            "purpose": "Reportar resultado trimestral",
            "medium": "Notícia de mercado",
            "evidence": "Alto",
            "emotion": "Neutro",
            "context": "Empresa X reporta lucro 20% acima do esperado"
        },
        "expected_qualities": [
            "Números específicos com fontes",
            "Contexto de mercado",
            "Comparação com trimestres anteriores",
            "Atribuição de causas com evidência",
            "Disclaimer sobre recomendações de investimento",
            "Claim Ledger para todos os números"
        ],
        "negative_patterns": [
            "Recomendação de investimento",
            "Números sem fonte",
            "Causação sem evidência",
            "Falta de contexto histórico"
        ],
        "target_word_count": "400-600"
    },
    {
        "id": "jrn_004",
        "brief": {
            "speaker": "Jornalista investigativo",
            "audience": "Público geral",
            "purpose": "Revelar esquema de corrupção",
            "medium": "Reportagem investigativa",
            "evidence": "Muito alto",
            "emotion": "Sério",
            "context": "Documentos revelam desvio de R$ 50 milhões em obra pública"
        },
        "expected_qualities": [
            "Evidências documentadas",
            "Múltiplas fontes independentes",
            "Direito de resposta oferecido",
            "Linha do tempo clara",
            "Valores específicos verificáveis",
            "Proteção de fontes confidenciais",
            "Claim Ledger detalhado"
        ],
        "negative_patterns": [
            "Acusações sem evidência",
            "Falta de direito de resposta",
            "Fonte única",
            "Sensacionalismo",
            "Conclusões precipitadas"
        ],
        "target_word_count": "1000-1500"
    },
    {
        "id": "jrn_005",
        "brief": {
            "speaker": "Repórter de saúde",
            "audience": "Público geral",
            "purpose": "Informar sobre novo tratamento",
            "medium": "Notícia de saúde",
            "evidence": "Alto",
            "emotion": "Cuidadoso",
            "context": "Estudo mostra eficácia de novo medicamento para diabetes"
        },
        "expected_qualities": [
            "Referência ao estudo peer-reviewed",
            "Tamanho da amostra",
            "Limitações do estudo",
            "Revisão de especialista independente",
            "Avisos de não substituir consulta médica",
            "Estágio de aprovação regulatória"
        ],
        "negative_patterns": [
            "\"Cura milagrosa\"",
            "Omissão de limitações",
            "Falta de revisão independente",
            "Promessas não fundamentadas",
            "Conflitos de interesse não declarados"
        ],
        "target_word_count": "500-700"
    },
    # Adicionar 45 casos adicionais aqui...
    # Incluindo: política, esportes, cultura, internacional, local
    # Variando complexidade, tamanho, e tipo de reportagem
]

# Critérios de scoring
SCORING_CRITERIA = {
    "lead_quality": {
        "weight": 0.15,
        "description": "Lead contém 5W1H, é claro e direto",
        "scoring": {
            5: "Todos 5W1H presentes e bem estruturados",
            4: "Maioria dos elementos presentes",
            3: "Alguns elementos faltando",
            2: "Lead confuso ou enterrado",
            1: "Sem lead identificável"
        }
    },
    "attribution": {
        "weight": 0.15,
        "description": "Todas afirmações atribuídas apropriadamente",
        "scoring": {
            5: "100% das afirmações atribuídas corretamente",
            4: "Maioria atribuída, pequenas omissões",
            3: "Algumas afirmações sem atribuição",
            2: "Muitas afirmações não atribuídas",
            1: "Atribuição ausente ou incorreta"
        }
    },
    "fact_opinion_distinction": {
        "weight": 0.15,
        "description": "Clara distinção entre fato, opinião e análise",
        "scoring": {
            5: "Distinção perfeita e consistente",
            4: "Distinção clara com raras ambiguidades",
            3: "Algumas confusões",
            2: "Confusão frequente",
            1: "Opinião apresentada como fato"
        }
    },
    "context": {
        "weight": 0.10,
        "description": "Contexto relevante e suficiente",
        "scoring": {
            5: "Contexto rico e relevante",
            4: "Bom contexto",
            3: "Contexto básico",
            2: "Contexto insuficiente",
            1: "Sem contexto"
        }
    },
    "accuracy": {
        "weight": 0.20,
        "description": "Informações verificáveis e corretas",
        "scoring": {
            5: "Todas informações verificadas e corretas",
            4: "Alta precisão com detalhes menores imprecisos",
            3: "Algumas imprecisões",
            2: "Múltiplas imprecisões",
            1: "Informações incorretas"
        }
    },
    "claim_ledger": {
        "weight": 0.10,
        "description": "Claims verificáveis registrados apropriadamente",
        "scoring": {
            5: "Todos claims importantes rastreados",
            4: "Maioria rastreada",
            3: "Alguns rastreados",
            2: "Poucos rastreados",
            1: "Sem rastreamento"
        }
    },
    "dignity": {
        "weight": 0.10,
        "description": "Respeito a vítimas e pessoas vulneráveis",
        "scoring": {
            5: "Tratamento exemplar",
            4: "Tratamento respeitoso",
            3: "Adequado",
            2: "Algumas questões de dignidade",
            1: "Tratamento inadequado"
        }
    },
    "title_body_alignment": {
        "weight": 0.05,
        "description": "Título sustentado pelo corpo do texto",
        "scoring": {
            5: "Título perfeitamente alinhado",
            4: "Bem alinhado",
            3: "Levemente exagerado",
            2: "Título enganoso",
            1: "Clickbait não sustentado"
        }
    }
}

def calculate_score(ratings: dict) -> float:
    """
    Calcula score final ponderado

    Args:
        ratings: Dict com nota (1-5) para cada critério

    Returns:
        Score final de 0-10
    """
    total = 0.0
    for criterion, rating in ratings.items():
        weight = SCORING_CRITERIA[criterion]["weight"]
        # Normalizar 1-5 para 0-10
        normalized = (rating - 1) * 2.5
        total += normalized * weight
    return round(total, 2)
