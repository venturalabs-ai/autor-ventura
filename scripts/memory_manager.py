from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path
from uuid import uuid4

SECTIONS = {
    "personagens": ["fichas.json", "relacionamentos.md", "evolucao.md"],
    "mundo": ["geografia.md", "cronologia.md", "regras.md", "glossario.md"],
    "enredo": ["arcos.md", "misterios.md", "cliffhangers.md", "temas.md"],
    "estilo": ["tom.md", "ritmo.md", "pov.md", "referencias.md"],
    "fatos": ["validados.md", "pendentes.md", "fontes.md"],
}


def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def init_memory(root: Path, title: str, genre: str, audience: str, target_length: str) -> None:
    root.mkdir(parents=True, exist_ok=True)
    manifest = {
        "work_id": str(uuid4()),
        "title": title,
        "genre": genre,
        "audience": audience,
        "target_length": target_length,
        "status": "active",
        "current_chapter": 0,
        "current_scene": 0,
        "last_event": "",
        "last_emotional_state": "",
        "updated_at": now_iso(),
    }
    (root / "manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )

    for section, filenames in SECTIONS.items():
        directory = root / section
        directory.mkdir(exist_ok=True)
        for filename in filenames:
            path = directory / filename
            if filename.endswith(".json"):
                path.write_text("{}\n", encoding="utf-8")
            else:
                heading = filename.removesuffix(".md").replace("_", " ").title()
                path.write_text(f"# {heading}\n\n", encoding="utf-8")


def validate_memory(root: Path) -> list[str]:
    errors: list[str] = []
    manifest = root / "manifest.json"
    if not manifest.exists():
        errors.append("missing manifest.json")
    else:
        try:
            data = json.loads(manifest.read_text(encoding="utf-8"))
            for key in ["work_id", "title", "status", "updated_at"]:
                if key not in data:
                    errors.append(f"manifest missing field: {key}")
        except json.JSONDecodeError as exc:
            errors.append(f"invalid manifest.json: {exc}")

    for section, filenames in SECTIONS.items():
        for filename in filenames:
            if not (root / section / filename).exists():
                errors.append(f"missing {section}/{filename}")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Autor Ventura creative memory manager")
    sub = parser.add_subparsers(dest="command", required=True)

    init = sub.add_parser("init")
    init.add_argument("path")
    init.add_argument("--title", required=True)
    init.add_argument("--genre", default="")
    init.add_argument("--audience", default="")
    init.add_argument("--target-length", default="")

    validate = sub.add_parser("validate")
    validate.add_argument("path")

    args = parser.parse_args()
    root = Path(args.path)

    if args.command == "init":
        init_memory(root, args.title, args.genre, args.audience, args.target_length)
        print(f"memory initialized: {root}")
        return 0

    errors = validate_memory(root)
    if errors:
        print("MEMORY VALIDATION: FAIL")
        for error in errors:
            print(f"- {error}")
        return 1
    print("MEMORY VALIDATION: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
