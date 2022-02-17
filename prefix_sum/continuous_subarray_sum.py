# Time: O(n); Space: O(n)
def check_subarray_sum(nums, k):
    d = {0: -1}
    cur_sum = 0

    for i, n in enumerate(nums):
        cur_sum += n
        cur_sum %= k

        if cur_sum in d:
            if i - d[cur_sum] > 1:
                return True
        else:
            d[cur_sum] = i

    return False


# Test cases:
print(check_subarray_sum(nums=[23, 2, 4, 6, 7], k=6))
print(check_subarray_sum(nums=[23, 2, 6, 4, 7], k=6))
print(check_subarray_sum(nums=[23, 2, 6, 4, 7], k=13))
print(check_subarray_sum(nums=[1, 5], k=2))
