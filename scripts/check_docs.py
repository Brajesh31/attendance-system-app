#!/usr/bin/env python3
"""Validate local Markdown links and balanced fenced code blocks."""

from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
MARKDOWN = sorted(
    {ROOT / "README.md", *ROOT.glob("*.md"), *ROOT.glob("docs/**/*.md"), *ROOT.glob(".github/**/*.md")}
)
LINK_RE = re.compile(r'(?<!!)\[[^\]]*\]\(([^)]+)\)')
FENCE_OPEN = re.compile(r'^\s{0,3}(`{3,}|~{3,})(.*)$')


def validate_file(path: Path) -> list[str]:
    errors = []
    lines = path.read_text(encoding="utf-8").splitlines()
    fence_char = None
    fence_len = 0

    for line_number, line in enumerate(lines, start=1):
        if fence_char is not None:
            closing = re.match(r'^\s{0,3}(' + re.escape(fence_char) + r'{' + str(fence_len) + r',})\s*$', line)
            if closing:
                fence_char = None
                fence_len = 0
            continue

        opening = FENCE_OPEN.match(line)
        if opening:
            marker = opening.group(1)
            fence_char = marker[0]
            fence_len = len(marker)
            continue

        for raw in LINK_RE.findall(line):
            target = raw.strip().split("#", 1)[0].split("?", 1)[0]
            if not target or target.startswith(("http://", "https://", "mailto:", "tel:")):
                continue
            candidate = (path.parent / target).resolve()
            if not candidate.exists():
                errors.append(f"{path.relative_to(ROOT)}:{line_number}: missing local target {target}")

    if fence_char is not None:
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
