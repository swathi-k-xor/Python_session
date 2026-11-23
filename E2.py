# `data/readings.txt` holds temperature readings, one per line, but some lines are not numbers. Write `parse_readings(lines)` that returns `(values, bad)`: `values` is a list of floats, `bad` is a list of `(line_number, text)` for lines that cannot be converted (line numbers start at 1; text is stripped). Print: the number of lines, the number of valid readings, the list of invalid line numbers, each invalid line as `  line <n>: <text as repr>`, the average with two decimals, and the minimum and maximum.

# ### Sample input

# `data/readings.txt` (30 lines).

# ### Expected output

# ```text
# Lines: 30
# Valid: 26
# Invalid lines: [4, 7, 17, 23]
#   line 4: 'N/A'
#   line 7: 'abc'
#   line 17: 'error'
#   line 23: ''
# Average: 26.99
# Min: 21.5  Max: 120.5
# ```


from pathlib import Path


def parse_readings(lines):
    values = []
    bad = []

    for line_number, line in enumerate(lines, start=1):
        text = line.strip()
        try:
            values.append(float(text))
        except ValueError:
            bad.append((line_number, text))

    return values, bad


if __name__ == "__main__":
    lines = Path(r"C:\Users\Swathi.K\Downloads\Python Training -Interns\Python Training -Interns\04-exception-handling\data\readings.txt").read_text(
        encoding="utf-8"
    ).splitlines()

    values, bad = parse_readings(lines)

    print(f"Lines: {len(lines)}")
    print(f"Valid: {len(values)}")
    print(f"Invalid lines: {[line_number for line_number, _ in bad]}")

    for line_number, text in bad:
        print(f"  line {line_number}: {text!r}")

    average = sum(values) / len(values)
    print(f"Average: {average:.2f}")
    print(f"Min: {min(values):g}  Max: {max(values):g}")