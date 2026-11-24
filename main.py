#!/usr/bin/env python3
"""One Line of Earned Pride — make.fun entry.

Writes exactly one line (1-240 characters) to /output/entry.txt:
a quiet, earned moment of pride for someone in a scene.
"""
import os

LINE = "After three winters of black skies and failed seedlings, the old fisherman's garden bloomed into forty pomegranates, and he offered the first one to the girl who had learned to name every star from his weather-beaten hands."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = LINE
    if not 1 <= len(text) <= 240:
        raise ValueError(f"line is {len(text)} chars (must be 1-240)")
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(text + "\n")
    os.chmod(path, 0o644)
    print(f"wrote {path} ({len(text)} chars)")


if __name__ == "__main__":
    main()
