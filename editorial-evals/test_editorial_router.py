import unittest

from scripts.editorial_router import normalize_medium, route


class EditorialRouterTests(unittest.TestCase):
    def test_aliases(self):
        self.assertEqual(normalize_medium("jornal"), "newspaper")
        self.assertEqual(normalize_medium("TV"), "broadcast")
        self.assertEqual(normalize_medium("monografia"), "academic")
        self.assertEqual(normalize_medium("votos"), "ceremonial")

    def test_academic_is_critical(self):
        decision = route("pesquisador", "banca", "defender tese", "doutorado")
        self.assertEqual(decision.medium, "academic")
        self.assertEqual(decision.evidence_level, "critical")
        self.assertIn("reference_integrity", decision.checks)

    def test_ceremonial_is_intimate_but_safe(self):
        decision = route("noivo", "noiva", "expressar compromisso", "casamento")
        self.assertEqual(decision.medium, "ceremonial")
        self.assertEqual(decision.emotion_level, "intimate")
        self.assertIn("consent", decision.checks)
        self.assertIn("privacy", decision.checks)

    def test_edital_has_risk_gate(self):
        decision = route("empresa", "comissão", "responder edital", "edital")
        self.assertEqual(decision.evidence_level, "critical")
        self.assertIn("requirement_matrix", decision.checks)
        self.assertIn("risk_flag", decision.checks)

    def test_unknown_medium_falls_back_to_general(self):
        decision = route("autor", "leitor", "explicar", "newsletter experimental")
        self.assertEqual(decision.medium, "general")


if __name__ == "__main__":
    unittest.main()
