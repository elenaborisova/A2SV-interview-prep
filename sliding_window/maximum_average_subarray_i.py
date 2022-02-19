# Time: O(n); Space: O(1)
def find_max_average(nums, k):
    max_average = float('-inf')
    cur_sum = l = r = 0

    while r < len(nums):
        cur_sum += nums[r]

        if r - l + 1 == k:
            max_average = max(max_average, cur_sum)
            cur_sum -= nums[l]
            l += 1
        r += 1

    return max_average / k


def find_max_average2(nums, k):
    cur_sum = sum(nums[:k])
    max_average = cur_sum

    for i in range(k, len(nums)):
        cur_sum += nums[i] - nums[i - k]
        max_average = max(max_average, cur_sum)

    return max_average / k


# Test cases:
print(find_max_average(nums=[1, 12, -5, -6, 50, 3], k=4))
