# Time: O(log n); Space: O(1)
def search_range(nums, target):
    n = len(nums)
    low, high = 0, n - 1
    while low <= high:
        mid = low + (high - low) // 2

        if nums[mid] >= target:
            high = mid - 1
        else:
            low = mid + 1
    start = low if low < n and nums[low] == target else -1

    high = n - 1
    while low <= high:
        mid = low + (high - low) // 2

        if nums[mid] <= target:
            low = mid + 1
        else:
            high = mid - 1
    end = high if high >= 0 and nums[high] == target else -1

    return [start, end]


# Test cases:
print(search_range(nums=[5, 7, 7, 8, 8, 10], target=8))
print(search_range(nums=[5, 7, 7, 8, 8, 10], target=6))
print(search_range(nums=[], target=0))
print(search_range(nums=[2, 2], target=3))
