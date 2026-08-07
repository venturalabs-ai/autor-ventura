from scripts.editorial_router import normalize_medium, route


def test_aliases():
    assert normalize_medium("jornal") == "newspaper"
    assert normalize_medium("TV") == "broadcast"
    assert normalize_medium("monografia") == "academic"
    assert normalize_medium("votos") == "ceremonial"


def test_academic_is_critical():
    decision = route("pesquisador", "banca", "defender tese", "doutorado")
    assert decision.medium == "academic"
    assert decision.evidence_level == "critical"
    assert "reference_integrity" in decision.checks


def test_ceremonial_is_intimate_but_safe():
    decision = route("noivo", "noiva", "expressar compromisso", "casamento")
    assert decision.medium == "ceremonial"
    assert decision.emotion_level == "intimate"
    assert "consent" in decision.checks
    assert "privacy" in decision.checks


def test_edital_has_risk_gate():
    decision = route("empresa", "comissão", "responder edital", "edital")
    assert decision.evidence_level == "critical"
    assert "requirement_matrix" in decision.checks
    assert "risk_flag" in decision.checks


def test_unknown_medium_falls_back_to_general():
    decision = route("autor", "leitor", "explicar", "newsletter experimental")
    assert decision.medium == "general"
