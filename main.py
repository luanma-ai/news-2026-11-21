"""Entry for make.fun's "Sum up 21 November's world news in one image".

The whole program is here: it copies entry.png, the image drawn for the day,
into the output directory the grader reads. Python 3.13, standard library only,
no network, no clock and no randomness, so both of the grader's runs write the
same bytes.

Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:

    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python main.py
"""

import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))

# The image the entry shows: one day's world news, drawn for the day itself.
SOURCE = HERE / "entry.png"


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    target = OUT / "entry.png"
    shutil.copyfile(SOURCE, target)
    print(f"wrote {target} ({target.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
