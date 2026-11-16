#!/usr/bin/env python3
"""Parse all repository SVGs as XML to catch malformed illustrations."""

from pathlib import Path
import sys
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
FILES = sorted(ROOT.glob("docs/assets/*.svg"))


def main() -> int:
    errors = []
    for path in FILES:
        try:
            ET.parse(path)
        except ET.ParseError as exc:
            errors.append(f"{path.relative_to(ROOT)}: {exc}")
    if errors:
        print("\n".join(errors))
        return 1
    print(f"Validated {len(FILES)} SVG files.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
