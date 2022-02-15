# Time: O(n); Space: O(1)
def min_subarray_len(target, nums):
    min_len, cur_sum = len(nums) + 1, 0

    l = r = 0
    while r < len(nums):
        cur_sum += nums[r]

        while cur_sum >= target and l < len(nums):
            min_len = min(min_len, r - l + 1)
            cur_sum -= nums[l]
            l += 1
        r += 1

    return min_len if min_len <= len(nums) else 0


# Test cases:
print(min_subarray_len(7, [2, 3, 1, 2, 4, 3]))
print(min_subarray_len(4, [1, 4, 4]))
print(min_subarray_len(11, [1, 1, 1, 1, 1, 1, 1, 1]))
