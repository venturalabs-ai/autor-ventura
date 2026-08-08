#!/usr/bin/env python3
"""Validate .github/skills/*/SKILL.md against Ventura baseline contract."""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(".github/skills")
NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


def validate() -> list[str]:
    errors: list[str] = []
    if not ROOT.exists():
        return ["missing .github/skills"]

    seen_names: set[str] = set()
    seen_descriptions: dict[str, str] = {}
    skill_files = sorted(ROOT.glob("*/SKILL.md"))
    if not skill_files:
        return [".github/skills has no SKILL.md files"]

    for skill_file in skill_files:
        rel = skill_file.as_posix()
        lines = skill_file.read_text(encoding="utf-8").splitlines()
        if not lines or lines[0].strip() != "---":
            errors.append(f"{rel}: missing opening frontmatter")
            continue
        try:
            close = next(i for i, line in enumerate(lines[1:], start=1) if line.strip() == "---")
        except StopIteration:
            errors.append(f"{rel}: missing closing frontmatter")
            continue

        fields: dict[str, str] = {}
        for line in lines[1:close]:
            if ":" not in line:
                continue
            key, value = line.split(":", 1)
            fields[key.strip()] = value.strip()

        name = fields.get("name", "")
        description = fields.get("description", "")
        folder = skill_file.parent.name
        body = lines[close + 1 :]

        if not (2 <= len(name) <= 64 and NAME_RE.fullmatch(name)):
            errors.append(f"{rel}: invalid kebab-case name")
        if name != folder:
            errors.append(f"{rel}: name must equal folder {folder}")
        if name in seen_names:
            errors.append(f"{rel}: duplicate name {name}")
        seen_names.add(name)

        if not description:
            errors.append(f"{rel}: description required")
        else:
            low = description.lower()
            if ": " in description:
                errors.append(f"{rel}: description must not contain colon-space")
            if "<" in description or ">" in description:
                errors.append(f"{rel}: description must not contain angle brackets")
            if "use when" not in low:
                errors.append(f"{rel}: description must include 'use when'")
            if "do not use when" not in low:
                errors.append(f"{rel}: description must include 'do not use when'")
            if description in seen_descriptions:
                errors.append(
                    f"{rel}: duplicate description also used by {seen_descriptions[description]}"
                )
            seen_descriptions[description] = rel

        if not any(line.strip() for line in body):
            errors.append(f"{rel}: empty body")
        if len(body) > 200:
            errors.append(f"{rel}: body exceeds 200 lines")

    return errors


def main() -> int:
    errors = validate()
    if errors:
        print("SKILL VALIDATION: FAIL")
        for err in errors:
            print(f"- {err}")
        return 1
    print(f"SKILL VALIDATION: PASS ({len(list(ROOT.glob('*/SKILL.md')))} skills)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
