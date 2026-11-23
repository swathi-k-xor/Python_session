# Write three functions using `re`:

# - `starts_with_number(text)` - `True` if the text begins with digits (use `re.match`).
# - `first_number(text)` - the first run of digits anywhere in the text as an `int`, or `None` (use `re.search`).
# - `is_whole_number(text)` - `True` only if the whole text is digits (use `re.fullmatch`).

# For every string in the list below print one line: the string with `repr` left-aligned in width 12, then `match=`, `search=` and `fullmatch=` with the results (each result left-aligned in width 5, except the last).

# ### Sample input

# ```python
# samples = ["42 apples", "apples 42", "42", "forty-two", ""]
# ```

import re


def starts_with_number(text):
    return re.match(r"\d+", text) is not None


def first_number(text):
    match = re.search(r"\d+", text)
    if match is None:
        return None
    return int(match.group())


def is_whole_number(text):
    return re.fullmatch(r"\d+", text) is not None


if __name__ == "__main__":
    samples = ["42 apples", "apples 42", "42", "forty-two", ""]

    for text in samples:
        match_result = starts_with_number(text)
        search_result = first_number(text)
        fullmatch_result = is_whole_number(text)

        print(
            f"{text!r:<12} "
            f"match={str(match_result):<5} "
            f"search={str(search_result):<5} "
            f"fullmatch={fullmatch_result}"
        )