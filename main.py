"""laugh-lab: a one-liner entry for the One-Liner Laugh Lab bounty.

The joke is a food-critic review of a sock, written straight-faced:
tasting notes (laundry detergent and despair), a two-star rating, and
the meal itself objecting — it kept screaming all the way down.

The program is just that one line, guarded by a small set of sanity
checks so the line we ship is exactly the line we wrote: no stray
whitespace, no hidden characters, no accidental overflow, and a
length the judges will accept.
"""

LINE = "The sock had notes of laundry detergent and despair, but I gave it two stars because it kept screaming all the way down."
MAX_CHARS = 200

OUT_PATH = "/output/entry.txt"


def _has_forbidden_char(text):
    """True if text contains a newline, carriage return, tab, or any
    other control character (anything below U+0020 or the DEL char)."""
    for ch in text:
        if ord(ch) < 0x20 or ord(ch) == 0x7F:
            return True
    return False


def check_line(text):
    """Raise ValueError if the entry line breaks any of the rules.

    Rules: it must not be empty, it must not start or end with
    whitespace, it must be a single line with no control characters,
    and it must fit inside MAX_CHARS.
    """
    if not text:
        raise ValueError("entry line is empty")
    if text != text.strip():
        raise ValueError("entry line has leading or trailing whitespace")
    if _has_forbidden_char(text):
        raise ValueError("entry line contains a newline, tab, or control character")
    if len(text) > MAX_CHARS:
        raise ValueError(
            f"entry line is {len(text)} characters, over the {MAX_CHARS}-character limit"
        )


def main():
    check_line(LINE)
    with open(OUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(LINE + "\n")


if __name__ == "__main__":
    main()
