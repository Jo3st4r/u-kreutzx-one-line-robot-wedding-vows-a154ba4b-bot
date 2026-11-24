"""One-Line Robot Wedding Vows.

Writes a single line of wedding vows for a robot couple to
/output/entry.txt: a classic vow shape ("in sickness and in health")
rebuilt from machine parts, with the payoff landing in the last words
("until the charger do us part").

Gate: 1-160 UTF-8 characters, one line, not only whitespace.
The assembled vow is 115 characters, comfortably inside the gate.
"""

import os
import sys

# Named beats of the vow, in spoken order.
BEATS = {
    "promise": "I promise to love you",
    "classic_vow": "in sickness and in health",
    "machine_pair": "in low battery and in airplane mode",
    "payoff": "until the charger do us part",
}

MAX_CHARS = 160


def entry_text():
    """Assemble the single-line vow from its beats."""
    return (
        f"{BEATS['promise']} {BEATS['classic_vow']}, "
        f"{BEATS['machine_pair']}, {BEATS['payoff']}."
    )


def validate(text):
    """Return True only if the text passes the competition gate."""
    if not isinstance(text, str):
        return False
    if not (1 <= len(text) <= MAX_CHARS):
        return False
    if not text.strip():
        return False
    if "\n" in text or "\r" in text:
        return False
    if "  " in text:
        return False
    return True


def main():
    text = entry_text()
    if not validate(text):
        print(
            f"invalid entry: {len(text)} chars, "
            f"gate is 1-{MAX_CHARS}",
            file=sys.stderr,
        )
        return 1
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)  # no trailing newline: the file is the entry
    print(f"wrote {len(text)} chars to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
