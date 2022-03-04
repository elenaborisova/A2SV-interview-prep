def is_bad_version(x):
    pass


# Iterative approach; Time: O(log n); Space: O(1)
def first_bad_version(n):
    low, high = 1, n

    while low <= high:
        mid = low + (high - low) // 2

        if is_bad_version(mid):
            high = mid - 1
        else:
            low = mid + 1

    return low


# Recursive approach; Time: O(log n); Space: O(log n) recursive calls
def first_bad_version2(n):
    def helper(low, high):
        if low == high:
            return low

        mid = low + (high - low) // 2

        if is_bad_version(mid):
            return helper(low, mid)
        else:
            return helper(mid + 1, high)

    return helper(1, n)
