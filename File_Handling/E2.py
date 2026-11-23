# Open `data/notes.txt` with a `with` statement and `encoding="utf-8"`. Print the first 5 lines, each preceded by its line number (right-aligned in width 3, then a colon and a space). Then write `file_stats(path)` that returns a dictionary with `lines`, `words`, `characters` (not counting the line ending) and `blank` (lines that are empty or only spaces), and print the four values.

# ### Sample input

# `data/notes.txt` (25 lines, one of them blank).

from pathlib import Path


def write_squares(path, n):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)

    with open(path, "w", encoding="utf-8") as file:
        for i in range(1, n + 1):
            file.write(f"{i} squared is {i * i}\n")

    return n


path = Path("output/squares.txt")
count = write_squares(path, 8)
print(f"Lines written: {count}")

with open(path, encoding="utf-8") as file:
    print(file.read(), end="")