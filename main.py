#!/usr/bin/env python3
"""Render the news of 20 November 2026 into a single image.

This program locates ``entry.png`` next to this file and copies it to
``/output/entry.png``, creating the output directory when needed.

The entry image itself is a fixed, pre-rendered illustration summing up
the day's world news in one picture. The program is intentionally small
and deterministic: running it twice on the same input produces the same
output bytes, because it only copies the file without modification.

Standard library only; requires Python 3.13 or newer.
"""

from __future__ import annotations

import hashlib
import shutil
import sys
from pathlib import Path


SOURCE_NAME = "entry.png"
# The competition harness reads the finished image from /output/entry.png.
OUTPUT_DIR = Path("/output")
OUTPUT_PATH = OUTPUT_DIR / SOURCE_NAME
CHUNK_SIZE = 1024 * 1024  # bytes read per chunk when hashing the output


def locate_source() -> Path:
    """Return the path of entry.png sitting next to this script."""
    source = Path(__file__).resolve().parent / SOURCE_NAME
    if not source.is_file():
        raise FileNotFoundError(f"entry image not found: {source}")
    return source


def copy_entry(source: Path, destination: Path) -> Path:
    """Copy the entry image to the destination, creating parents."""
    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(source, destination)
    return destination


def sha256_of(path: Path) -> str:
    """Return the hex SHA-256 digest of a file's bytes."""
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(CHUNK_SIZE), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main() -> int:
    source = locate_source()
    output = copy_entry(source, OUTPUT_PATH)
    size = output.stat().st_size
    checksum = sha256_of(output)
    print(f"Wrote {output} ({size} bytes, sha256={checksum})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
