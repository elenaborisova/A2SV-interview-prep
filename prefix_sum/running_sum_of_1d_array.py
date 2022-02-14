# Time: O(n); Space: O(1)
def running_sum(nums):
    cur_sum = 0

    for i, n in enumerate(nums):
        cur_sum += n
        nums[i] = cur_sum

    return nums


# Time: O(n); Space: O(1)
def running_sum2(nums):
    for i in range(1, len(nums)):
        nums[i] += nums[i - 1]

    return nums


# Test cases:
print(running_sum([1, 2, 3, 4]))
print(running_sum([1, 1, 1, 1, 1]))
print(running_sum([3, 1, 2, 10, 1]))
