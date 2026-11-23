# Write recursive functions:

# - `sum_of_digits(n)`: sum of the decimal digits of an integer (ignore the sign: `-907` gives `16`).
# - `reverse_string(text)`: the string reversed, without `[::-1]` or `reversed()`.
# - `is_palindrome(text)`: `True` if the text reads the same forwards and backwards, ignoring case and any
#   character that is not a letter or digit. The empty string is a palindrome. (Cleaning the text with a
#   comprehension first is fine; the comparison itself must be recursive.)

# ### Sample input

# Your solution must work with this driver code, placed at the bottom of your file:

# ```python
# print(sum_of_digits(12345))
# print(sum_of_digits(-907))
# print(sum_of_digits(0))
# print(reverse_string("recursion"))
# print(repr(reverse_string("")))
# print(is_palindrome("A man, a plan, a canal: Panama"))
# print(is_palindrome("Python"))
# print(is_palindrome(""))
# ```


def sum_of_digits(n):
    n = abs(n)
    if n < 10:
        return n
    return n % 10 + sum_of_digits(n // 10)


def reverse_string(text):
    if len(text) <= 1:
        return text
    return reverse_string(text[1:]) + text[0]


def is_palindrome(text):
    cleaned = "".join(
        character.lower() for character in text if character.isalnum()
    )

    if len(cleaned) <= 1:
        return True

    return (
        cleaned[0] == cleaned[-1]
        and is_palindrome(cleaned[1:-1])
    )


if __name__ == "__main__":
    print(sum_of_digits(12345))
    print(sum_of_digits(-907))
    print(sum_of_digits(0))
    print(reverse_string("recursion"))
    print(repr(reverse_string("")))
    print(is_palindrome("A man, a plan, a canal: Panama"))
    print(is_palindrome("Python"))
    print(is_palindrome(""))