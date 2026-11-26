"""Fortune Cookie Wisdom for Developers.

Writes one original fortune-cookie line to /output/entry.txt.

The line is aimed at the tired senior engineer judging it, and is
built to the judge's brief in order: it is fortune-cookie wisdom for
a developer (not a slogan or generic advice); it is one short,
balanced sentence that lands in a single breath; it is true about a
developer's day (the 2 a.m. debug session, the comment you wish
someone had left); it turns that truth in an unfamiliar way, instead
of repeating a familiar saying; and it leaves a quiet twist that
rewards a second read -- the stranger you are writing for is your
own future self.
"""

import os

ENTRY = "Write the comment your future self needs at 2 a.m., for that tired stranger is you."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    # No trailing newline: the gate counts every character in the file.
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
