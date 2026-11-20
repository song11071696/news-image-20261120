"""Publish the bundled news image for make.fun news-image-20261120.

This script copies the entry image that ships with this repository to
``/output/entry.png`` and then checks the copy byte for byte against the
source. It uses only the Python standard library and makes no network
calls, so two runs always produce an identical file.
"""

from __future__ import annotations

import hashlib
import shutil
import sys
from pathlib import Path

SOURCE_FILENAME = "entry.png"
DESTINATION = Path("/output/entry.png")
PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"


def locate_source() -> Path:
    """Return the path of the entry image bundled next to this script."""
    here = Path(__file__).resolve().parent
    return here / SOURCE_FILENAME


def digest_file(image_path: Path) -> str:
    """Return the SHA-256 hex digest of the file at ``image_path``."""
    hasher = hashlib.sha256()
    with image_path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            hasher.update(block)
    return hasher.hexdigest()


def copy_image(origin: Path, target: Path) -> int:
    """Copy ``origin`` to ``target`` and return the number of bytes copied."""
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(origin, target)
    return target.stat().st_size


class EntryPublisher:
    """Copy the bundled entry image to /output and verify the result."""

    def __init__(self, origin: Path, target: Path) -> None:
        self.origin = origin
        self.target = target

    def verify_copy(self) -> None:
        """Check the output exists, matches the source size and hash.

        Exits with a non-zero status and a message on stderr if any
        check fails, so a bad copy can never pass silently.
        """
        if not self.target.exists():
            print(f"error: output missing: {self.target}", file=sys.stderr)
            raise SystemExit(1)
        with self.target.open("rb") as handle:
            header = handle.read(len(PNG_SIGNATURE))
        if header != PNG_SIGNATURE:
            print(
                "error: output is not a PNG file "
                f"(bad magic bytes: {header!r})",
                file=sys.stderr,
            )
            raise SystemExit(1)
        source_size = self.origin.stat().st_size
        target_size = self.target.stat().st_size
        if target_size != source_size:
            print(
                f"error: size mismatch: source {source_size} bytes, "
                f"output {target_size} bytes",
                file=sys.stderr,
            )
            raise SystemExit(1)
        source_hash = digest_file(self.origin)
        target_hash = digest_file(self.target)
        if target_hash != source_hash:
            print(
                f"error: sha256 mismatch: source {source_hash}, "
                f"output {target_hash}",
                file=sys.stderr,
            )
            raise SystemExit(1)

    def run(self) -> int:
        """Copy the image, verify it, and report the result."""
        copied_bytes = copy_image(self.origin, self.target)
        self.verify_copy()
        print(f"Wrote {self.target} ({copied_bytes} bytes)")
        return 0


def main() -> int:
    """Locate the bundled image, publish it, and verify the output."""
    source = locate_source()
    if not source.exists():
        print(f"error: bundled source image not found: {source}", file=sys.stderr)
        print(
            "error: expected entry.png next to main.py in the repository",
            file=sys.stderr,
        )
        return 2
    publisher = EntryPublisher(source, DESTINATION)
    return publisher.run()


if __name__ == "__main__":
    raise SystemExit(main())
