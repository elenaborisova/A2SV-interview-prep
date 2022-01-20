# Bubble sort
# Time: O(n^2); Space: O(1)
def sort_colors(nums):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] > nums[j]:
                nums[j], nums[i] = nums[i], nums[j]


# Counting sort
# Time: O(n^2) or O(n) ?; Space: O(1)
def sort_colors2(nums):
    count = [0] * 3  # Space O(1)
    for n in nums:  # Time O(n)
        count[n] += 1

    pos = 0
    for i, n in enumerate(count):  # Time O(1)
        for j in range(pos, pos + n):  # Time O(n)
            nums[j] = i
        pos += n


# Dutch National Flag partitioning problem
# Time: O(n); Space: O(1)
def sort_colors3(nums):
    p0, p2 = 0, len(nums) - 1

    i = 0
    while i <= p2:
        if nums[i] == 0:
            nums[i], nums[p0] = nums[p0], nums[i]
            p0 += 1
            i += 1
        elif nums[i] == 2:
            nums[i], nums[p2] = nums[p2], nums[i]
            p2 -= 1
        else:
            i += 1


# Test cases:
print(sort_colors3([2, 0, 2, 1, 1, 0]))
print(sort_colors3([2, 0, 1]))
