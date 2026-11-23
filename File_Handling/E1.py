# Open `data/notes.txt` with a `with` statement and `encoding="utf-8"`. Print the first 5 lines, each preceded by its line number (right-aligned in width 3, then a colon and a space). Then write `file_stats(path)` that returns a dictionary with `lines`, `words`, `characters` (not counting the line ending) and `blank` (lines that are empty or only spaces), and print the four values.

# ### Sample input

# `data/notes.txt` (25 lines, one of them blank).

def file_stats(path):
    lines = 0
    words = 0
    characters = 0
    blank = 0

    with open(path, encoding="utf-8") as file:
        for line in file:
            text = line.rstrip("\n")
            lines += 1
            words += len(text.split())
            characters += len(text)
            if not text.strip():
                blank += 1

    return {
        "lines": lines,
        "words": words,
        "characters": characters,
        "blank": blank,
    }

path = r"C:\Users\Swathi.K\Downloads\Python Training -Interns\Python Training -Interns\03-file-handling\data\notes.txt"

with open(path, encoding="utf-8") as file:
    for number, line in enumerate(file, start=1):
        if number > 5:
            break
        print(f"{number:3}: {line.rstrip('\n')}")

stats = file_stats(path)
print(f"Lines: {stats['lines']}")
print(f"Words: {stats['words']}")
print(f"Characters: {stats['characters']}")
print(f"Blank lines: {stats['blank']}")