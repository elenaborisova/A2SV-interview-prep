# Time: O(n^2); Space: O(1)
def remove_duplicates(nums):
    i = 1

    while i < len(nums):
        if nums[i] == nums[i - 1]:
            nums.pop(i)
        else:
            i += 1

    return len(nums)


# Without removing duplicates; Time: O(n); Space: O(1)
def remove_duplicates2(nums):
    pos = 1

    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]:
            nums[pos] = nums[i]
            pos += 1

    return pos


# Test cases:
print(remove_duplicates2([1, 1, 2]))
print(remove_duplicates2([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
