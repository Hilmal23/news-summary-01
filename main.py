#!/usr/bin/env python3
"""news-summary-01: write the stored summary of 11 November 2026 world news
to the grader's output file. Deterministic, stdlib only, no network: the
summary text lives in summary.txt next to this file and is copied byte for
byte, so two runs always write the same bytes.
"""
import os
from pathlib import Path

HERE = Path(__file__).resolve().parent
MAX_CHARS = 2000


def main():
    summary = (HERE / "summary.txt").read_bytes()
    text = summary.decode("utf-8")
    # Gate (from the competition rules): 1 to 2,000 Unicode code points,
    # at least one non-whitespace character. Fail loudly instead of
    # submitting an invalid entry.
    if not (1 <= len(text) <= MAX_CHARS) or not text.strip():
        raise SystemExit(f"summary is {len(text)} chars, outside 1-2000")
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_bytes(summary)


if __name__ == "__main__":
    main()
