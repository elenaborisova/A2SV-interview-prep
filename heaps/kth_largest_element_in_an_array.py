import heapq


# Time: O(n log k); Space: O(1)
def find_kth_largest(nums, k):
    return heapq.nlargest(k, nums)[-1]


# Test cases:
print(find_kth_largest(nums=[3, 2, 1, 5, 6, 4], k=2))
print(find_kth_largest(nums=[3, 2, 3, 1, 2, 4, 5, 5, 6], k=4))
