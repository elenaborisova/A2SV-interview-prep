from collections import deque


# Time: O(n^2); Space: O(n)
def max_subarray_sum_circular(nums):
    max_sum = prefix = nums[0]
    nums = deque(nums)

    for i in range(len(nums)):

        for j in range(1, len(nums)):
            if prefix > 0:
                prefix += nums[j]
            else:
                prefix = nums[j]
            max_sum = max(max_sum, prefix)

        nums.append(nums.popleft())
        prefix = 0

    return max_sum


# Time: O(n); Space: O(1)
def max_subarray_sum_circular2(nums):
    min_sum = max_sum = max_prefix = min_prefix = nums[0]

    for j in range(1, len(nums)):
        max_prefix = max(max_prefix + nums[j], nums[j])
        max_sum = max(max_sum, max_prefix)

        min_prefix = min(min_prefix + nums[j], nums[j])
        min_sum = min(min_sum, min_prefix)

    max_sum2 = sum(nums) - min_sum
    return max(max_sum, max_sum2) if max_sum >= 0 else max_sum


# Test cases:
print(max_subarray_sum_circular2([1, -2, 3, -2]))
print(max_subarray_sum_circular2([5, -3, 5]))
print(max_subarray_sum_circular2([-3, -2, -3]))
