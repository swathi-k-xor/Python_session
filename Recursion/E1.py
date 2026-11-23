# Write three recursive functions:

# - `factorial(n)`: `n! = n * (n-1)!`, with `0! = 1! = 1`. Negative `n` raises `ValueError("n must be non-negative")`.
# - `countdown(n)`: returns the list `[n, n-1, ..., 1]`; for `n <= 0` return an empty list.
# - `sum_list(numbers)`: the sum of a list of numbers without using `sum()` or loops.

# ### Sample input

# Your solution must work with this driver code, placed at the bottom of your file:

# ```python
# print(factorial(0), factorial(1), factorial(5))
# print(factorial(20))
# print(countdown(5))
# print(countdown(0))
# print(sum_list([1, 2, 3, 4]))
# print(sum_list([]))
# try:
#     factorial(-3)
# except ValueError as err:
#     print("Error:", err)
# ```

# ### Expected output

# ```text
# 1 1 120
# 2432902008176640000
# [5, 4, 3, 2, 1]
# []
# 10
# 0
# Error: n must be non-negative
# ```

def factorial(n):
    if n < 0:
        raise ValueError("n must be non-negative")
    if n <= 1:
        return 1
    return n * factorial(n - 1)


def countdown(n):
    if n <= 0:
        return []
    return [n] + countdown(n - 1)


def sum_list(numbers):
    if not numbers:
        return 0
    return numbers[0] + sum_list(numbers[1:])


if __name__ == "__main__":
    print(factorial(0), factorial(1), factorial(5))
    print(factorial(20))
    print(countdown(5))
    print(countdown(0))
    print(sum_list([1, 2, 3, 4]))
    print(sum_list([]))

    try:
        factorial(-3)
    except ValueError as err:
        print("Error:", err)