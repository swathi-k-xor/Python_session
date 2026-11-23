# Write `bubble_sort(items)` and `selection_sort(items)`. Each returns a tuple
# `(sorted_copy, swaps)` and leaves the input list unchanged. Bubble sort must stop early if a
# whole pass makes no swaps.

# ### Sample input

# ```python
# data = [64, 25, 12, 22, 11]
# print("input:    ", data)
# print("bubble:   ", bubble_sort(data))
# print("selection:", selection_sort(data))
# print("already sorted bubble:", bubble_sort([1, 2, 3, 4]))
# print("input unchanged:", data)
# ```

def bubble_sort(items):
    result = list(items)
    swaps = 0

    for pass_num in range(len(result) - 1):
        swapped = False

        for i in range(len(result) - pass_num - 1):
            if result[i] > result[i + 1]:
                result[i], result[i + 1] = result[i + 1], result[i]
                swaps += 1
                swapped = True

        if not swapped:
            break

    return result, swaps


def selection_sort(items):
    result = list(items)
    swaps = 0

    for i in range(len(result) - 1):
        min_index = i

        for j in range(i + 1, len(result)):
            if result[j] < result[min_index]:
                min_index = j

        if min_index != i:
            result[i], result[min_index] = result[min_index], result[i]
            swaps += 1

    return result, swaps


if __name__ == "__main__":
    data = [64, 25, 12, 22, 11]

    print("input:    ", data)
    print("bubble:   ", bubble_sort(data))
    print("selection:", selection_sort(data))
    print("already sorted bubble:", bubble_sort([1, 2, 3, 4]))
    print("input unchanged:", data)