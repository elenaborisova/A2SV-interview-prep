# Time: O(n log n); Space: O(n)
def target_indices(nums, target):
    nums.sort()

    ans = []
    for i, n in enumerate(nums):
        if n == target:
            ans.append(i)

    return ans


# Time: O(n + k); Space(n + k)
def target_indices2(nums, target):
    count = [0] * (max(nums) + 1)
    for n in nums:
        count[n] += 1

    sorted_nums = []
    for i, n in enumerate(count):
        if n != 0:
            sorted_nums.extend([i] * n)

    ans = []
    for i, n in enumerate(sorted_nums):
        if n == target:
            ans.append(i)

    return ans


# Time: O(n); Space: O(n)
def target_indices3(nums, target):
    less, equal = 0, 0

    for num in nums:
        if num < target:
            less += 1

        if num == target:
            equal += 1

    return list(range(less, less + equal))


# Test cases:
print(target_indices2([1, 2, 5, 2, 3], 2))
print(target_indices2([1, 2, 5, 2, 3], 3))
print(target_indices2([1, 2, 5, 2, 3], 5))
