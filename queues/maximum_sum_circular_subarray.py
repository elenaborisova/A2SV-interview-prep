from collections import deque


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


# Test cases:
print(max_subarray_sum_circular([1, -2, 3, -2]))
print(max_subarray_sum_circular([5, -3, 5]))
print(max_subarray_sum_circular([-3, -2, -3]))
