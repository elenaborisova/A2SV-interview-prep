from collections import defaultdict


# Brute Force; Time: O(n^2); Space: O(1)
def subarray_sum(nums, k):
    res = 0
    cur_sum = 0

    for i in range(len(nums)):
        cur_sum += nums[i]
        if cur_sum == k:
            res += 1

        for j in range(i + 1, len(nums)):
            cur_sum += nums[j]
            if cur_sum == k:
                res += 1

        cur_sum = 0

    return res


# Time: O(n); Space: O(n)
def subarray_sum2(nums, k):
    d = defaultdict(int)
    d[0] = 1
    count, presum = 0, 0

    for n in nums:
        presum += n

        if presum - k in d:
            count += d[presum - k]

        d[presum] += 1

    return count


# Test cases:
print(subarray_sum2(nums=[1, 1, 1], k=2))
print(subarray_sum2(nums=[1, 2, 3], k=3))
print(subarray_sum2(nums=[3, 3, 3, 1, 2], k=3))
print(subarray_sum2(nums=[1], k=0))
print(subarray_sum2(nums=[-1, -1, 1], k=0))
print(subarray_sum2(nums=[1, 2, 3, 4, 1, 2, 3], k=3))
print(subarray_sum2(nums=[1, -1, 0], k=0))
