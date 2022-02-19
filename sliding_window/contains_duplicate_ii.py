import collections


# Using dictionary; Time: O(n); Space: O(n)
def contains_nearby_duplicate(nums, k):
    d = {}

    for i, n in enumerate(nums):
        if n in d and i - d[n] <= k:
            return True
        d[n] = i

    return False


# Sliding window; Time: O(n); Space: O(n)
def contains_nearby_duplicate2(nums, k):
    d = collections.defaultdict(int)

    i, j = 0, 0
    while j < len(nums):
        if j > k:
            d[nums[i]] -= 1
            i += 1

        if d[nums[j]] > 0:
            return True

        d[nums[j]] += 1
        j += 1

    return False


# Test cases:
print(contains_nearby_duplicate2(nums=[1, 2, 3, 1], k=3))
print(contains_nearby_duplicate2(nums=[1, 0, 1, 1], k=1))
print(contains_nearby_duplicate2(nums=[1, 2, 3, 1, 2, 3], k=2))
print(contains_nearby_duplicate2(nums=[1, 2, 1], k=0))
print(contains_nearby_duplicate2(nums=[0, 1, 2, 3, 2, 5], k=3))
