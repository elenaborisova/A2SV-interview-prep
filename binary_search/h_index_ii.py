# Time: O(log n); Space: O(1)
def hIndex(citations):
    n = len(citations)
    low, high = 0, n - 1

    while low <= high:
        mid = low + (high - low) // 2

        if n - mid == citations[mid]:
            return citations[mid]
        elif n - mid > citations[mid]:
            low = mid + 1
        else:
            high = mid - 1

    return n - low


# Test cases:
print(hIndex([0]))
print(hIndex([100]))
print(hIndex([1, 8, 9, 10]))
print(hIndex([0, 1, 2, 3, 7, 8]))
