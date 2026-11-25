"""Entry for make.fun bounty "The Tired Dark Lord: A 100-Word Villain Monologue".

A dark lord, done with the whole villain business, leaves the gate open on
purpose -- not mercy, arithmetic. The weariness never gets named; it lives
in the deflection: a dragon retired on a pension of sheep, a lieutenant
who unionised, skeletons filing for overtime, an amulet pawned for a
mattress with actual springs. The last beat turns the throne itself into
the punchline: free, checked, and squeaking.
"""

from pathlib import Path

TEXT = "The hero comes at dawn — they always do, right on schedule, sword polished, speech rehearsed. I have left the gate unbarred. Not mercy. Arithmetic. My dragon retired to a cave with a pension of sheep. My lieutenant unionised. The skeletons filed for overtime, and the prophecy had a typo anyway. The cursed amulet? I pawned it for a mattress with actual springs. Let the boy have his legend; I have a kettle, a blanket, and a map with no X on it. Conquer the world, he says. Someone else can. The throne is free — I checked. It squeaks."

OUT = Path("/output/entry.txt")


def check_len(text, lo=1, hi=600):
    size = len(text)
    assert lo <= size <= hi, f"entry must be {lo}-{hi} chars, got {size}"
    return size


def check_words(text, n=100):
    count = len(text.split())
    assert count == n, f"entry must be {n} words, got {count}"
    return count


def save_line(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as fh:
        fh.write(text)


def main():
    check_len(TEXT)
    check_words(TEXT)
    save_line(OUT, TEXT)


if __name__ == "__main__":
    main()
