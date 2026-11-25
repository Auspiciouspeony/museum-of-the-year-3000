#!/usr/bin/env python3
"""Museum of the Year 3000 — make.fun entry (program/v1, Python 3.13).

Writes one museum label — the line a museum in the year 3000 puts
beside an ordinary object from today — to /output/entry.txt.

Deterministic by design: the label is a fixed string, no randomness,
no clock, no network, no environment reads. Two runs write the same
bytes. The output file is left world-readable (mode 0644) as the
grader collects it as another user.
"""

import os

LABEL = (
    "Traffic Light, c. 2020. Red meant stop, green meant go, "
    "and yellow meant go faster."
)


def main() -> None:
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # Exact bytes, no trailing newline: the gate counts characters,
    # and the tie-break favours fewer bytes.
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LABEL)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
