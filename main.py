import os
from pathlib import Path

summary = Path(__file__).with_name("summary.txt").read_bytes()
# Guard the submission size before creating the output file.
if not 1 <= len(summary) <= 2000:
    raise ValueError("summary.txt must contain 1-2,000 bytes")

output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
output_dir.mkdir(parents=True, exist_ok=True)
(output_dir / "entry.txt").write_bytes(summary)
