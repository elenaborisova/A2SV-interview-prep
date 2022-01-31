# Time: O(n); Space: O(1)
def max_subarray(nums):
    max_sum = nums[0]
    pre_sum = nums[0]

    for i in range(1, len(nums)):
        if pre_sum < 0:
            pre_sum = nums[i]
        else:
            pre_sum += nums[i]

        max_sum = max(max_sum, pre_sum)

    return max_sum


def max_subarray2(nums):
    for i in range(1, len(nums)):
        if nums[i - 1] > 0:
            nums[i] += nums[i - 1]

    return max(nums)


# Test cases:
print(max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
