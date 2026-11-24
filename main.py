"""The worst app idea ever pitched: NapTrack Pro.

NapTrack Pro is an AI app that detects the exact moment you fall asleep
on the couch, then wakes you up with a push notification to tell you that
you fell asleep on the couch, because an unwitnessed nap doesn't count.
The joke is airtight uselessness: the app's entire purpose is to defeat
itself. It solves the one problem nobody has (not knowing you napped)
by creating the one problem everyone hates (being woken up), and the
founder's deadpan justification, that a nap only counts if you are told
about it, is delivered with total confidence.

Why it reads like a real pitch: it has a product name, a plausible tech
hook (AI detection), a concrete user (the couch napper) and a vivid
scene anyone can picture, phone buzzing in a dark living room while the
napper blinks awake. The uselessness is not a bug in the pitch, it is
the pitch: every word the founder would say to sell it is also the
reason nobody on earth needs it.
"""

ENTRY = (
    "NapTrack Pro is an AI app that detects the exact moment you fall "
    "asleep on the couch, then wakes you up with a push notification "
    "to tell you that you fell asleep on the couch, because an "
    "unwitnessed nap doesn't count."
)

# One sentence, 217 characters; with the trailing newline the file is
# 218 characters, inside the 1-240 character gate.
assert 1 <= len(ENTRY) + 1 <= 240 and ENTRY.strip(), (
    "ENTRY plus newline must be 1-240 chars, non-blank"
)


def write_entry(path, text):
    """Write the entry text to path as UTF-8 and set mode 0644."""
    import os

    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    os.chmod(path, 0o644)


def main():
    import os

    text = ENTRY + "\n"
    try:
        os.makedirs("/output", exist_ok=True)
        write_entry("/output/entry.txt", text)
    except OSError:
        os.makedirs("./output", exist_ok=True)
        write_entry("./output/entry.txt", text)
    print(ENTRY)


if __name__ == "__main__":
    main()
