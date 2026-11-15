"""Entry program for the make.fun competition "Make the AI judge excited".

The entry is a single image, entry.png, stored beside this file. This
program copies it, byte for byte, into the output directory named by the
MAKEFUN_OUTPUT_DIR environment variable (or an "out" folder when the
variable is not set), as entry.png.

Standard library only. No network access, no randomness, no arguments:
running it twice over the same repository always writes the same bytes.
"""

import os
import shutil
import sys


def main() -> int:
    here = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(here, "entry.png")

    if not os.path.isfile(source):
        print(f"error: {source} is missing", file=sys.stderr)
        return 1

    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or os.path.join(here, "out")
    destination = os.path.join(output_dir, "entry.png")

    os.makedirs(output_dir, exist_ok=True)
    shutil.copyfile(source, destination)

    size = os.path.getsize(destination)
    if size == 0:
        print(f"error: wrote an empty file to {destination}", file=sys.stderr)
        return 1

    print(f"Wrote {destination} ({size} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
