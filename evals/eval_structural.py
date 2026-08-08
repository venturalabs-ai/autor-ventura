"""Offline baseline evals for Autor Ventura.

These checks validate repository contracts and required specialist artifacts.
They do not claim to measure model-level writing quality; semantic/model evals
should be added separately with fixed datasets and model/version metadata.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = [
    "01-pesquisador.md",
    "02-arquiteto-narrativo.md",
    "03-escritor-de-voz.md",
    "04-humanizador.md",
    "05-formatador.md",
    "06-conector-emocional.md",
    "07-revisor-final.md",
]


def main() -> None:
    failures: list[str] = []
    for name in REQUIRED:
        path = ROOT / name
        if not path.is_file():
            failures.append(f"missing: {name}")
            continue
        text = path.read_text(encoding="utf-8")
        if len(text.strip()) < 500:
            failures.append(f"too small: {name}")
        if "#" not in text:
            failures.append(f"no markdown headings: {name}")

    if failures:
        raise SystemExit("Structural eval failed:\n- " + "\n- ".join(failures))

    print(f"PASS: {len(REQUIRED)} required specialist artifacts validated")
    print("Scope: structural contract only; no semantic/model-quality claim")


if __name__ == "__main__":
    main()
