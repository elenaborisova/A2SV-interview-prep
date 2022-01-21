from functools import cmp_to_key


def largest_number(nums):
    nums = [str(n) for n in nums]
    nums.sort(key=cmp_to_key(lambda a, b: 1 if a + b > b + a else -1), reverse=True)
    return '0' if nums[0] == '0' else ''.join(nums)


# Test cases:
print(largest_number([3, 30, 34, 5, 9]))
print(largest_number([34323, 3432]))
print(largest_number([0, 0]))
