"""Entry for make.fun's "Sum up 21 November's world news in one image".

The program is small on purpose: the day's work is the picture, and the
picture is a file in the repository. What this code has to get right is the
part the grader actually runs -- write exactly one image to /output/entry.png,
at the size the kit asks for, from a source that is there or fail loudly.

Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:

    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python main.py
"""

import os
import shutil
import sys
from pathlib import Path

# The image lives beside the entrypoint at the repository's root; this source
# may sit one directory down, so the root is the source's parent's parent here
# and the packed entrypoint's own directory when it is packed.
HERE = Path(__file__).resolve().parent
ROOT = HERE.parent if HERE.name == "src" else HERE
NAME = "entry.png"


def out_dir() -> Path:
    """Where the grader reads the entry from, or MAKEFUN_OUTPUT_DIR locally."""
    return Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))


def main() -> int:
    source = ROOT / NAME
    if not source.is_file():
        print(f"missing {source}", file=sys.stderr)
        return 1

    target = out_dir() / NAME
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(source, target)

    size = target.stat().st_size
    print(f"wrote {target} ({size} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
