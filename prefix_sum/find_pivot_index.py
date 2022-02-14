# Time: O(n); Space: O(n)
def pivot_index(nums):
    n = len(nums)
    left_prefix_sum = nums.copy()
    right_prefix_sum = nums.copy()

    for i in range(1, n):
        left_prefix_sum[i] += left_prefix_sum[i - 1]
        right_prefix_sum[n - i - 1] += right_prefix_sum[n - i]

    for i in range(len(nums)):
        if left_prefix_sum[i] == right_prefix_sum[i]:
            return i
    return -1


# Time: O(n); Space: O(1)
def pivot_index2(nums):
    left, right = 0, sum(nums)

    for i, n in enumerate(nums):
        right -= n
        if left == right:
            return i
        left += n

    return -1


# Test cases:
print(pivot_index([1, 7, 3, 6, 5, 6]))
print(pivot_index([1, 2, 3]))
print(pivot_index([2, 1, -1]))
print(pivot_index([2]))
print(pivot_index([-1, -1, -1, -1, -1, 0]))
print(pivot_index([-1, -1, -1, 0, 1, 1]))
