# Time: O(log n); Space: O(1)
def search(nums, target):
    low, high = 0, len(nums) - 1

    while low <= high:
        mid = low + (high - low) // 2

        if nums[mid] == target:
            return mid

        if nums[low] <= nums[mid]:
            if target > nums[mid] or target < nums[low]:
                low = mid + 1
            else:
                high = mid - 1
        else:
            if target < nums[mid] or target > nums[high]:
                high = mid - 1
            else:
                low = mid + 1

    return -1


# Test cases:
print(search(nums=[4, 5, 6, 7, 0, 1, 2], target=0))
print(search(nums=[1], target=0))
print(search(nums=[5, 1, 3], target=3))
