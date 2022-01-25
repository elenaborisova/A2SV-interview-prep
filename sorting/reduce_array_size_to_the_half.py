from collections import Counter


# Time: (n log n); Space: O(n)
def min_set_size(arr):
    counter = Counter(arr)
    counter = dict(sorted(counter.items(), key=lambda x: x[1], reverse=True))
    set_size = 0
    removed_count = 0

    for n in counter:
        removed_count += counter[n]
        set_size += 1

        if len(arr) - removed_count <= len(arr) // 2:
            return set_size

    return set_size


# Test cases:
print(min_set_size([3, 3, 3, 3, 5, 5, 5, 2, 2, 7]))
print(min_set_size([7, 7, 7, 7, 7, 7]))
