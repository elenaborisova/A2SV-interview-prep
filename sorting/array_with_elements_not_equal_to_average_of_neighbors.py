# Brute Force approach; Time: O(n^2); Space: O(1)
def rearrange_array(nums):
    i = 1
    flag = True

    while True:
        while i < len(nums) - 1:
            if nums[i - 1] + nums[i + 1] == nums[i] * 2:
                nums[i + 1], nums[i] = nums[i], nums[i + 1]
                flag = False
            else:
                i += 1

        if flag:
            break
        else:
            flag = True
            i = 1

    return nums


# Time: O(n log n); Space: O(1)
def rearrange_array2(nums):
    nums.sort()

    for i in range(1, len(nums), 2):
        nums[i], nums[i - 1] = nums[i - 1], nums[i]

    return nums


# Test cases:
print(rearrange_array2([1, 2, 3, 4, 5]))
print(rearrange_array2([6, 2, 0, 9, 7]))
print(rearrange_array2([10, 7, 5, 4, 3]))
print(rearrange_array2([1, 2, 5, 9]))
