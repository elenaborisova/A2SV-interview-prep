# Time: O(n); Space: O(n)
def min_start_value(nums):
    cum_nums = []
    cur_sum = 0

    for n in nums:
        cur_sum += n
        cum_nums.append(cur_sum)

    min_value = min(cum_nums)
    return 1 if min_value > 0 else 1 - min_value


# Time: O(n); Space: O(1)
def min_start_value2(nums):
    cur_sum, min_value = 0, 0

    for n in nums:
        cur_sum += n
        min_value = min(min_value, cur_sum)

    return 1 - min_value


print(min_start_value([-3, 2, -3, 4, 2]))
print(min_start_value([1, 2]))
print(min_start_value([1, -2, -3]))
print(min_start_value([2, 3, 5, -5, -1]))
