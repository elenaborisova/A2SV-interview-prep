import collections


def number_of_subarrays(nums, k):
    # Replace even numbers with 0 and odd numbers with 1
    for i, n in enumerate(nums):
        if n % 2 == 0:
            nums[i] = 0
        else:
            nums[i] = 1

    # Transform nums into prefix sum array
    for i in range(1, len(nums)):
        nums[i] += nums[i - 1]

    # Calculate result
    d = collections.defaultdict(int)
    d[0] = 1
    res = 0

    for n in nums:
        if n - k in d:
            res += d[n - k]
        d[n] += 1

    return res


def number_of_subarrays2(nums, k):
    i = count = nice_count = odd_count = 0

    for j in range(len(nums)):
        if nums[j] % 2 == 1:
            odd_count += 1
            count = 0

        while odd_count == k:
            odd_count -= nums[i] % 2
            i += 1
            count += 1
        nice_count += count

    return nice_count


# Test cases:
print(number_of_subarrays(nums=[1, 1, 2, 1, 1], k=3))
print(number_of_subarrays(nums=[2, 4, 6], k=1))
print(number_of_subarrays(nums=[2, 2, 2, 1, 2, 2, 1, 2, 2, 2], k=2))
