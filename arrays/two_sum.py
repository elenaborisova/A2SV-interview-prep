# Time: O(n); Space: O(n)
def two_sum(nums, target):
    d = {}

    for i, n in enumerate(nums):
        m = target - n

        if m in d:
            return [d[m], i]

        d[n] = i


# Test cases:
print(two_sum([2, 7, 11, 15], 9))
print(two_sum([3, 2, 4], 6))
print(two_sum([3, 3], 6))
