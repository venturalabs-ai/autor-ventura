from __future__ import annotations

from dataclasses import dataclass, asdict
from typing import Literal
import argparse
import json

Medium = Literal[
    "newspaper", "broadcast", "magazine", "book", "edital",
    "academic", "symposium", "ceremonial", "technical", "general"
]
Evidence = Literal["low", "moderate", "high", "critical"]
Emotion = Literal["contained", "balanced", "expressive", "intimate"]


@dataclass
class EditorialDecision:
    speaker: str
    audience: str
    purpose: str
    medium: Medium
    evidence_level: Evidence
    emotion_level: Emotion
    limits: list[str]
    pack: str
    checks: list[str]


MEDIUM_RULES: dict[str, dict[str, object]] = {
    "newspaper": {
        "pack": "journalism/README.md",
        "evidence": "high",
        "emotion": "contained",
        "checks": ["5W1H", "attribution", "headline_support", "claim_ledger", "respect_review"],
    },
    "broadcast": {
        "pack": "broadcast/README.md",
        "evidence": "high",
        "emotion": "balanced",
        "checks": ["speakability", "duration", "attribution", "claim_ledger", "respect_review"],
    },
    "magazine": {
        "pack": "publication-packs/magazine.md",
        "evidence": "high",
        "emotion": "balanced",
        "checks": ["nut_graph", "scene_basis", "attribution", "claim_ledger", "respect_review"],
    },
    "book": {
        "pack": "prompts/autor-ventura-v2.md",
        "evidence": "moderate",
        "emotion": "expressive",
        "checks": ["memory", "continuity", "voice_consistency", "fact_boundary", "respect_review"],
    },
    "edital": {
        "pack": "publication-packs/editais.md",
        "evidence": "critical",
        "emotion": "contained",
        "checks": ["requirement_matrix", "evidence_match", "deadline_check", "document_gap", "risk_flag"],
    },
    "academic": {
        "pack": "academic/README.md",
        "evidence": "critical",
        "emotion": "contained",
        "checks": ["reference_integrity", "method_alignment", "evidence_strength", "limitations", "authorship_boundary"],
    },
    "symposium": {
        "pack": "publication-packs/symposium.md",
        "evidence": "critical",
        "emotion": "balanced",
        "checks": ["cross_format_consistency", "time_fit", "reference_integrity", "limitations", "audience_fit"],
    },
    "ceremonial": {
        "pack": "ceremonial/README.md",
        "evidence": "low",
        "emotion": "intimate",
        "checks": ["authenticity", "consent", "privacy", "specificity", "respect_review"],
    },
    "technical": {
        "pack": "01-pesquisador.md",
        "evidence": "critical",
        "emotion": "contained",
        "checks": ["terminology", "source_validation", "units", "risk_language", "review_required"],
    },
    "general": {
        "pack": "voice-engine/README.md",
        "evidence": "moderate",
        "emotion": "balanced",
        "checks": ["audience_fit", "purpose_fit", "clarity", "respect_review"],
    },
}

ALIASES = {
    "jornal": "newspaper", "noticia": "newspaper", "notícia": "newspaper",
    "tv": "broadcast", "radio": "broadcast", "rádio": "broadcast", "video": "broadcast", "vídeo": "broadcast",
    "revista": "magazine", "longform": "magazine",
    "livro": "book", "romance": "book",
    "edital": "edital", "licitacao": "edital", "licitação": "edital",
    "monografia": "academic", "tcc": "academic", "dissertacao": "academic", "dissertação": "academic", "doutorado": "academic", "tese": "academic", "artigo cientifico": "academic", "artigo científico": "academic",
    "simposio": "symposium", "simpósio": "symposium", "congresso": "symposium",
    "votos": "ceremonial", "casamento": "ceremonial", "homenagem": "ceremonial", "discurso": "ceremonial",
    "tecnico": "technical", "técnico": "technical", "manual": "technical",
}


def normalize_medium(value: str) -> Medium:
    key = value.strip().lower()
    medium = ALIASES.get(key, key)
    return medium if medium in MEDIUM_RULES else "general"  # type: ignore[return-value]


def route(
    speaker: str,
    audience: str,
    purpose: str,
    medium: str,
    limits: list[str] | None = None,
    evidence_level: Evidence | None = None,
    emotion_level: Emotion | None = None,
) -> EditorialDecision:
    normalized = normalize_medium(medium)
    rule = MEDIUM_RULES[normalized]
    return EditorialDecision(
        speaker=speaker.strip() or "autor não definido",
        audience=audience.strip() or "público não definido",
        purpose=purpose.strip() or "objetivo não definido",
        medium=normalized,
        evidence_level=evidence_level or rule["evidence"],  # type: ignore[arg-type]
        emotion_level=emotion_level or rule["emotion"],  # type: ignore[arg-type]
        limits=limits or [],
        pack=str(rule["pack"]),
        checks=list(rule["checks"]),  # type: ignore[arg-type]
    )


def main() -> None:
    parser = argparse.ArgumentParser(description="Autor Ventura v3 editorial router")
    parser.add_argument("--speaker", required=True)
    parser.add_argument("--audience", required=True)
    parser.add_argument("--purpose", required=True)
    parser.add_argument("--medium", required=True)
    parser.add_argument("--limit", action="append", default=[])
    args = parser.parse_args()
    decision = route(args.speaker, args.audience, args.purpose, args.medium, args.limit)
    print(json.dumps(asdict(decision), ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
