import os
from pathlib import Path

summary = Path(__file__).with_name("summary.txt").read_bytes()
if not 1 <= len(summary) <= 2_000:
    raise ValueError("summary.txt must contain 1–2,000 bytes")
output = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
output.mkdir(parents=True, exist_ok=True)
(output / "entry.txt").write_bytes(summary)
