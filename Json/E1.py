# Using `json.dumps` and `json.loads` on the dictionary below:

# 1. Print the compact JSON text (`compact: ...`).
# 2. Print an indented version (2 spaces) with sorted keys.
# 3. Write `roundtrip(obj)` that converts an object to JSON text and back. Show how the type of `scores` changes, what `married` and `nickname` become, and whether the round trip gives an equal object.
# 4. Show what happens to integer dictionary keys: print `roundtrip({1: "a", 2: "b"})`.
# 5. Try to dump a dictionary containing a `set`, catch the `TypeError` and print its message.

# ### Sample input

# ```python
# sample = {
#     "name": "Asha",
#     "age": 30,
#     "married": False,
#     "scores": (90, 85),
#     "nickname": None,
#     "height": 1.68,
# }
# ```

import json


def roundtrip(obj):
    return json.loads(json.dumps(obj))


if __name__ == "__main__":
    sample = {
        "name": "Asha",
        "age": 30,
        "married": False,
        "scores": (90, 85),
        "nickname": None,
        "height": 1.68,
    }

    print("compact:", json.dumps(sample))

    print("indented:")
    print(json.dumps(sample, indent=2, sort_keys=True))

    restored = roundtrip(sample)
    print(
        f"scores type before: {type(sample['scores']).__name__} "
        f"| after: {type(restored['scores']).__name__}"
    )
    print(
        f"married after: {restored['married']} "
        f"| nickname after: {restored['nickname']}"
    )
    print("equal after round trip:", sample == restored)

    print("int keys:", roundtrip({1: "a", 2: "b"}))

    try:
        json.dumps({"values": {1, 2, 3}})
    except TypeError as err:
        print("TypeError:", err)