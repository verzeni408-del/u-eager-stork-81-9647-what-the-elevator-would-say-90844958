#!/usr/bin/env python3
"""Elevator monologue emitter.

Builds the competition entry from sentence fragments and writes the
finished line to the output file the harness reads.  Standard library
only; no third-party imports anywhere.
"""

import os


FRAGMENTS = (
    '"Sorry, I\'m full," I said to the guy holding the door open. ',
    "He stepped out. I was empty. ",
    "I just didn't like him.",
)


def assemble_entry(parts):
    """Join the stored fragments into the single entry string."""
    return "".join(parts)


def destination_path():
    """Resolve where the entry file must land."""
    return os.environ.get("OUTPUT_PATH", "/output/entry.txt")


def emit():
    """Write the assembled entry to its destination file."""
    text = assemble_entry(FRAGMENTS)
    target = destination_path()
    os.makedirs(os.path.dirname(target), exist_ok=True)
    with open(target, "w", encoding="utf-8") as handle:
        handle.write(text)


if __name__ == "__main__":
    emit()
