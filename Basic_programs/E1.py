# a whole number `n` (one line, no prompt text). Write a function `fizzbuzz(n)` that returns a list of strings for the numbers 1 to `n`: `"Fizz"` for multiples of 3, `"Buzz"` for multiples of 5, `"FizzBuzz"` for multiples of both, otherwise the number itself as text. Print one item per line.

# ### Sample input
# Read
# Typed into the program (standard input):

# ```text
# 15


def fizzbuzz(n):
    result = []

    for i in range(1, n + 1):
        if i % 15 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(i))

    return result


n = int(input("Enter a number: "))
for item in fizzbuzz(n):
    print(item)