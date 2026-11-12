"""Copy the dated news summary to the make.fun entry path."""

import os
from pathlib import Path


SOURCE = Path(__file__).with_name("summary.txt")


def main() -> None:
    content = SOURCE.read_bytes()
    length = len(content.decode("utf-8"))
    if not 1 <= length <= 2_000:
        raise ValueError("summary must contain 1 to 2,000 characters")
    destination = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")) / "entry.txt"
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_bytes(content)


if __name__ == "__main__":
    main()
