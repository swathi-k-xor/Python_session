# Part A - discovery. Open `test_calculator.py` and `extra_tests.py`. Run `py -m pytest -v` in the folder and look at what pytest found. Then find out why the other tests were ignored, using these default rules:

# - files are collected when the name matches `test_*.py` or `*_test.py`;
# - inside them, functions that start with `test` are collected;
# - classes are collected when the name starts with `Test` and has no `__init__`; methods inside must start with `test`.

# Fix the names so that every test in the two files is collected, and move the tests from `extra_tests.py` into `test_calculator.py` (give the file a correct name or merge it).

# Part B - write the tests. In `test_calculator.py` write plain tests with `assert` for:

# - `add`: two positive numbers, two negative numbers, and `add(0.1, 0.2)` compared with `pytest.approx(0.3)` (floating point numbers are not exact);
# - `subtract`: a normal case and a case with a negative result;
# - `multiply`: a normal case and multiplying by zero (put the multiply tests in a class named `TestMultiply`);
# - `divide`: `divide(10, 4)` is `2.5`, and the result is always a `float` (use `isinstance`).

# Dividing by zero raises an exception; you will test that in T15-E02.

# ### Behaviours to test

# | Function | Behaviour |
# |----------|-----------|
# | `add` | `add(2, 3) == 5`, `add(-2, -3) == -5`, `add(0.1, 0.2)` is about 0.3 |
# | `subtract` | `subtract(5, 3) == 2`, `subtract(3, 5) == -2` |
# | `multiply` | `multiply(4, 3) == 12`, `multiply(7, 0) == 0` |
# | `divide` | `divide(10, 4) == 2.5`, `divide(10, 5)` is a float |

"""A tiny calculator. This is the code under test: do not change it."""


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("cannot divide by zero")
    return a / b