#!/usr/bin/env python3
"""Compression eval — entry point (placeholder).

The implementation is tracked in DESIGN.md. This script currently only
prints a pointer to the design doc so nobody mistakes an unimplemented
harness for a broken one.

See scripts/compression_eval/DESIGN.md for the full proposal.
"""
from __future__ import annotations

import sys
from pathlib import Path


_DESIGN = Path(__file__).parent / "DESIGN.md"


def main() -> int:
    print("compression_eval: not implemented yet")
    print(f"See {_DESIGN} for the proposed design and open questions.")
    print()
    print("Implementation is landing in follow-up PRs, one fixture at a time.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
