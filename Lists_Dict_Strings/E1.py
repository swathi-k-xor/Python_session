# Problem

# Given the list `numbers`, write a function `list_stats(nums)` that returns a dictionary with the keys `max`, `min`, `total`, `average`, `descending` (a new list sorted from largest to smallest) and `every_second` (elements at index 0, 2, 4, ...). Then print the results exactly as shown. Do not change the original list.

# ### Sample input

# ```python
# numbers = [14, 3, 9, 27, 8, 21, 5, 18]
# ```

def list_stats(nums):
    return {
        "max": max(nums),
        "min": min(nums),
        "total": sum(nums),
        "average": sum(nums) / len(nums),
        "descending": sorted(nums, reverse=True),  # new sorted list
        "every_second": nums[::2]                  # index 0, 2, 4, ...
    }


# Given list
numbers = [14, 3, 9, 27, 8, 21, 5, 18]

stats = list_stats(numbers)

print(f"max: {stats['max']}")
print(f"min: {stats['min']}")
print(f"total: {stats['total']}")
print(f"average: {stats['average']:.2f}")
print(f"descending: {stats['descending']}")
print(f"every second: {stats['every_second']}")