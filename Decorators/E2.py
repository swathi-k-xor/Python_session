# A closure is an inner function that remembers variables from the function that created it.

# - `make_counter(start=0, step=1)` returns a function. The first call returns `start`, the next `start + step`,
#   and so on. Each counter keeps its own state (use `nonlocal`).
# - `make_multiplier(n)` returns a function that multiplies its argument by `n`.
# - `build_multipliers(factors)` returns a list of multiplier functions, one per factor.

# The driver also prints a "broken" list built with lambdas in a loop; study the output and explain why every
# function multiplies by 4.

# ### Sample input

# Your solution must work with this driver code, placed at the bottom of your file:

# ```python
# c1 = make_counter()
# c2 = make_counter(start=10, step=5)
# print(c1(), c1(), c1())
# print(c2(), c2())
# double = make_multiplier(2)
# print(double(21))
# print([f(10) for f in build_multipliers([2, 3, 4])])
# print(double.__closure__[0].cell_contents)
# broken = [lambda x: x * factor for factor in [2, 3, 4]]
# print([f(10) for f in broken])
# ```

def make_counter(start=0, step=1):
    current = start

    def counter():
        nonlocal current
        value = current
        current += step
        return value

    return counter


def make_multiplier(n):
    def multiplier(value):
        return value * n

    return multiplier


def build_multipliers(factors):
    return [make_multiplier(factor) for factor in factors]


if __name__ == "__main__":
    c1 = make_counter()
    c2 = make_counter(start=10, step=5)
    print(c1(), c1(), c1())
    print(c2(), c2())

    double = make_multiplier(2)
    print(double(21))
    print([f(10) for f in build_multipliers([2, 3, 4])])
    print(double.__closure__[0].cell_contents)

    broken = [lambda x: x * factor for factor in [2, 3, 4]]
    print([f(10) for f in broken])