# Time: O(n); Space: O(1)
def first_missing_positive(nums):
    # Replace negative values with 0
    for i, n in enumerate(nums):
        if n < 0:
            nums[i] = 0

    # Turn number negative if corresponding index is in range [1,...,len(nums) + 1]
    for i, n in enumerate(nums):
        if 1 <= abs(n) <= len(nums):
            val = abs(n)
            if nums[val - 1] > 0:
                nums[val - 1] *= -1
            elif nums[val - 1] == 0:
                nums[val - 1] = (len(nums) + 1) * -1

    # Loop through the range to find missing value
    for i, n in enumerate(nums):
        if n >= 0:
            return i + 1
    return len(nums) + 1


# Test cases:
print(first_missing_positive([1, 2, 0]))
print(first_missing_positive([3, 4, -1, 1]))
print(first_missing_positive([7, 8, 9, 11, 12]))
