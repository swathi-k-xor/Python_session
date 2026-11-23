# Functions can be stored in variables and dictionaries, passed to other functions and returned from them.

# Write:

# - `add(a, b)`, `sub(a, b)` and `mul(a, b)`.
# - A dictionary `OPERATIONS` mapping `"add"`, `"sub"` and `"mul"` to those functions (no `if/elif` chain).
# - `calculate(op_name, a, b)` that looks the operation up and calls it. For an unknown name raise
#   `ValueError(f"Unknown operation: {op_name}")`.
# - `apply_twice(func, value)` returning `func(func(value))`.
# - `compose(f, g)` returning a **new function** `h` such that `h(x) == f(g(x))`.

# ### Sample input

# Your solution must work with this driver code, placed at the bottom of your file:

# ```python
# print(calculate("add", 2, 3))
# print(calculate("mul", 4, 5))
# print(apply_twice(lambda s: s + "!", "hey"))
# shout = compose(str.upper, lambda s: s + "!")
# print(shout("hello"))
# print(add.__name__, callable(add), type(add).__name__)
# print(sorted(OPERATIONS))
# try:
#     calculate("pow", 2, 3)
# except ValueError as err:
#     print("Error:", err)
# ```

def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


OPERATIONS = {
    "add": add,
    "sub": sub,
    "mul": mul,
}


def calculate(op_name, a, b):
    try:
        operation = OPERATIONS[op_name]
    except KeyError:
        raise ValueError(f"Unknown operation: {op_name}") from None
    return operation(a, b)


def apply_twice(func, value):
    return func(func(value))


def compose(f, g):
    def h(x):
        return f(g(x))

    return h


if __name__ == "__main__":
    print(calculate("add", 2, 3))
    print(calculate("mul", 4, 5))
    print(apply_twice(lambda s: s + "!", "hey"))

    shout = compose(str.upper, lambda s: s + "!")
    print(shout("hello"))

    print(add.__name__, callable(add), type(add).__name__)
    print(sorted(OPERATIONS))

    try:
        calculate("pow", 2, 3)
    except ValueError as err:
        print("Error:", err)