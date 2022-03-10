# Time: O(n log n); Space: O(1)
def find_duplicate(nums):
    # 'low' and 'high' represent the range of values of the target
    low = 1
    high = len(nums) - 1

    while low <= high:
        cur = low + (high - low) // 2
        # Count how many numbers are less than or equal to 'cur'
        count = sum(num <= cur for num in nums)
        if count > cur:
            duplicate = cur
            high = cur - 1  # shrink the space to find the lowest value
        else:
            low = cur + 1

    return duplicate


# Floyd's cycle detection algorithm; Time: O(n); Space: O(1)
def find_duplicate2(nums):
    slow = fast = 0
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break

    slow2 = 0
    while True:
        slow = nums[slow]
        slow2 = nums[slow2]
        if slow == slow2:
            return slow


# Test cases:
print(find_duplicate2([1, 3, 4, 2, 2]))
