import collections


# Time: O(n); Space: O(n)
def get_max_distinct(nums, k):
    d = collections.defaultdict(int)
    res = 0

    l = r = 0
    while r < len(nums):
        d[nums[r]] += 1

        while len(d) > k:
            d[nums[l]] -= 1
            if d[nums[l]] == 0: del d[nums[l]]
            l += 1

        res += r - l + 1
        r += 1

    return res


def subarrays_with_k_distinct(nums, k):
    return get_max_distinct(nums, k) - get_max_distinct(nums, k - 1)


# Test cases:
print(subarrays_with_k_distinct(nums=[1, 2, 1, 2, 3], k=2))
print(subarrays_with_k_distinct(nums=[1, 2], k=1))
