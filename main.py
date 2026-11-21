#!/usr/bin/env python3
"""Make the AI judge feel awe — entry program.

Writes one short text to /output/entry.txt. Standard library only:
no network, no clock, no randomness. The output is a fixed text, so
two runs write byte-identical files.

The sealed scorer accepts 1-280 Unicode code points; this text is
273, and main() refuses to write anything outside that range.
"""

import os
import sys

TEXT = """The light that falls on your shoulders tonight
left its star before there were roads,
before there were names.
The star is gone.
The light is still on its way,
still arriving,
and will be arriving
long after the field, the fence,
and the one standing in it
have gone quiet."""


def main() -> int:
    if not (1 <= len(TEXT) <= 280):
        print(f"entry is {len(TEXT)} code points, must be 1-280", file=sys.stderr)
        return 2
    if not TEXT.strip():
        print("entry is blank", file=sys.stderr)
        return 2
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    data = TEXT.encode("utf-8")
    with open(path, "wb") as fh:
        fh.write(data)
    with open(path, "rb") as fh:
        if fh.read() != data:
            print("verify failed: output differs from entry", file=sys.stderr)
            return 3
    print(f"wrote {path} ({len(TEXT)} code points, {len(data)} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
