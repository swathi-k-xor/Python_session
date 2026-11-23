# Read lines from standard input until the input ends; skip blank lines. Each line should hold two numbers separated by a space. Write `divide_line(line)` that returns a message string:

# - Normal case: `<a> / <b> = <result>` using `:g` formatting for all three numbers (so `10.0` shows as `10`).
# - Division by zero: `Cannot divide by zero`.
# - Anything else wrong (not numbers, or not exactly two items): `Invalid input: expected two numbers`.

# Use `try`, specific `except` clauses and `else`; do not use a bare `except:`. Print the message for every line.

# ### Sample input

# Typed into the program (standard input):

# ```text
# 10 2
# 7 0
# x 3
# 5
# 7 2
# 1 2 3
# ```

import sys


def divide_line(line):
    try:
        a_text, b_text = line.split()
        a = float(a_text)
        b = float(b_text)
        result = a / b
    except ZeroDivisionError:
        return "Cannot divide by zero"
    except ValueError:
        return "Invalid input: expected two numbers"
    else:
        return f"{a:g} / {b:g} = {result:g}"


if __name__ == "__main__":
    for line in sys.stdin:
        if line.strip():
            print(divide_line(line))