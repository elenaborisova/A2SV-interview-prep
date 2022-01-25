def counting_sort(arr):
    frequencies = [0] * (max(arr) + 1)
    for n in arr:
        frequencies[n] += 1

    return frequencies


# Time: O(n + k); Space: O(n + k)
def counting_sort2(arr):
    frequencies = [0] * (max(arr) + 1)
    for n in arr:
        frequencies[n] += 1

    res = []
    for i, value in enumerate(frequencies):
        if value != 0:
            res += [i] * value

    return res


# Test cases:
print(counting_sort([1, 1, 3, 2, 1]))
