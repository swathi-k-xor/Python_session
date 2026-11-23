# Write `extract_numbers(text)` returning all numbers as strings (integers and decimals, with an optional minus sign), `extract_hashtags(text)` returning every `#word` (letters, digits and underscore), and `extract_pairs(text)` returning `(key, value)` tuples for every `key=value` in a string. Print the numbers, their sum rounded to 2 decimals, the hashtags, the pairs, and the pairs as a dictionary.

# ### Sample input

# ```python
# text = ("Order 1042 shipped on 14 March: 3 items, total 59.97 EUR, "
#         "discount -5.5 applied. Tags: #sale #newArrival #eco_friendly")
# settings = "mode=fast; retries=3; name=Zed; level=7"
# ```

import re


def extract_numbers(text):
    return re.findall(r"-?\d+(?:\.\d+)?", text)


def extract_hashtags(text):
    return re.findall(r"#\w+", text)


def extract_pairs(text):
    return re.findall(r"(\w+)=(\w+)", text)


if __name__ == "__main__":
    text = (
        "Order 1042 shipped on 14 March: 3 items, total 59.97 EUR, "
        "discount -5.5 applied. Tags: #sale #newArrival #eco_friendly"
    )
    settings = "mode=fast; retries=3; name=Zed; level=7"

    numbers = extract_numbers(text)
    hashtags = extract_hashtags(text)
    pairs = extract_pairs(settings)

    print("numbers:", numbers)
    print("sum:", round(sum(float(number) for number in numbers), 2))
    print("hashtags:", hashtags)
    print("pairs:", pairs)
    print("as dict:", dict(pairs))