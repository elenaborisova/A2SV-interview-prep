# Time: O(n); Space: O(1)
def max_sum_two_no_overlap(nums, first_len, second_len):
    for i in range(1, len(nums)):
        nums[i] += nums[i - 1]

    res = nums[first_len + second_len - 1]
    first_max = nums[first_len - 1]
    second_max = nums[second_len - 1]

    for i in range(first_len + second_len, len(nums)):
        # case 1: first_len subarray is always before second_len subarray
        first_max = max(first_max, nums[i - second_len] - nums[i - first_len - second_len])
        # case 1: second_len subarray is always before first_len subarray
        second_max = max(second_max, nums[i - first_len] - nums[i - first_len - second_len])
        # compare two cases and update result
        res = max(res, first_max + nums[i] - nums[i - second_len], second_max + nums[i] - nums[i - first_len])

    return res


# Test cases:
print(max_sum_two_no_overlap([2, 1, 5, 6, 0, 9, 5, 0, 3, 8], 4, 3) == 31)
print(max_sum_two_no_overlap([3, 8, 1, 3, 2, 1, 8, 9, 0], 3, 2) == 29)
print(max_sum_two_no_overlap([0, 6, 5, 2, 2, 5, 1, 9, 4], 1, 2) == 20)
print(max_sum_two_no_overlap([4, 5, 14, 16, 16, 20, 7, 13, 8, 15], 3, 5) == 109)
