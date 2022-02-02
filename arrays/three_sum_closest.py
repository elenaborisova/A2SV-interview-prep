# Time: O(n^2); Space: O(n)
def three_sum_closest(nums, target):
    nums.sort()
    closest_sum = 1000

    for i in range(len(nums) - 2):
        n = nums[i]
        l, r = i + 1, len(nums) - 1

        while l < r:
            cur_sum = n + nums[l] + nums[r]
            if cur_sum == target:
                return target

            if abs(cur_sum - target) < abs(closest_sum - target):
                closest_sum = cur_sum

            if cur_sum > target:
                r -= 1
            else:
                l += 1

    return closest_sum


# Test cases:
print(three_sum_closest([-1, 2, 1, -4], 1))
print(three_sum_closest([0, 0, 0], 1))
