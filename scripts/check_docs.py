#!/usr/bin/env python3
"""Validate local Markdown links and Mermaid fenced blocks without dependencies."""

from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
MARKDOWN = sorted(
    {ROOT / "README.md", *ROOT.glob("*.md"), *ROOT.glob("docs/**/*.md"), *ROOT.glob(".github/**/*.md")}
)
LINK_RE = re.compile(r'(?<!!)\[[^\]]*\]\(([^)]+)\)')
MERMAID_START = re.compile(r'^\s*```mermaid\s*$')
FENCE = re.compile(r'^\s*```\s*$')


def validate_file(path: Path) -> list[str]:
    errors = []
    text = path.read_text(encoding="utf-8")
    in_fence = False
    for line_number, line in enumerate(text.splitlines(), start=1):
        if MERMAID_START.match(line):
            if in_fence:
                errors.append(f"{path.relative_to(ROOT)}:{line_number}: nested Mermaid fence")
            in_fence = True
            continue
        if FENCE.match(line):
            in_fence = not in_fence
            continue
        for raw in LINK_RE.findall(line):
            target = raw.strip().split("#", 1)[0].split("?", 1)[0]
            if not target or target.startswith(("http://", "https://", "mailto:", "tel:")):
                continue
            candidate = (path.parent / target).resolve()
            if not candidate.exists():
                errors.append(f"{path.relative_to(ROOT)}:{line_number}: missing local target {target}")
    if in_fence:
        errors.append(f"{path.relative_to(ROOT)}: unclosed fenced code block")
    return errors


def main() -> int:
    errors = []
    for path in MARKDOWN:
        if path.exists():
            errors.extend(validate_file(path))
    if errors:
        print("\n".join(errors))
        return 1
    print(f"Validated {sum(p.exists() for p in MARKDOWN)} Markdown files.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
