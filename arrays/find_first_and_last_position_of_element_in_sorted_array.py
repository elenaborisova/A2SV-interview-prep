def binary_search(nums, target, left_bias):
    low, high = 0, len(nums) - 1
    i = -1

    while low <= high:
        mid = (low + high) // 2

        if target > nums[mid]:
            low = mid + 1
        elif target < nums[mid]:
            high = mid - 1
        else:
            i = mid
            if left_bias:
                high = mid - 1
            else:
                low = mid + 1

    return i


# Time: O(log n); Space: O(1)
def search_range(nums, target):
    left = binary_search(nums, target, True)
    right = binary_search(nums, target, False)
    return [left, right]


# Test cases:
print(search_range([5, 7, 7, 8, 8, 10], 8))
print(search_range([5, 7, 7, 8, 8, 10], 6))
print(search_range([], 0))
print(search_range([1], 1))
