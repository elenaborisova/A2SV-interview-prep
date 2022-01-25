# Counting Sort; Time: O(n); Space: O(n)
from collections import deque


def find_original_array(changed):
    count = [0] * (max(changed) + 1)
    for n in changed:
        count[n] += 1

    original = []
    for n, c in enumerate(count):
        if c == 0:
            continue

        double = n * 2
        if n == 0 and c % 2 == 0:
            original.extend([n] * (c // 2))
        elif double < len(count) and count[double] >= c:
            original.extend([n] * c)
            count[n] -= c
            count[double] -= c
        else:
            return []

    return original


# Queue; Time: O(n log n); Space: O(n)
def find_original_array2(changed):
    arr = sorted(changed)
    dq = deque([])
    res = []

    for i in arr:
        if dq and i == dq[0]:
            dq.popleft()
        else:
            dq.append(2 * i)
            res.append(i)

    if dq:
        return []
    return res


# Test cases:
print(find_original_array([1, 3, 4, 4, 2, 6, 8, 8]))
print(find_original_array([6, 3, 0, 1]))
print(find_original_array([1]))
print(find_original_array([4, 4]))
print(find_original_array([0, 0, 0, 0]))
print(find_original_array([2, 1, 2, 4, 2, 4]))
