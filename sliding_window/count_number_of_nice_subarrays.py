# 27min
def number_of_subarrays(nums, k):
    count = 0
    res = 0

    l, r = 0, 0
    while r < len(nums):

        while count < k and r < len(nums):
            if nums[r] % 2 != 0:
                count += 1
            r += 1
        r -= 1

        while nums[l] % 2 == 0:
            res += 1
            l += 1
        l -= 1

        r += 1

    return res


print(number_of_subarrays(nums = [1,1,2,1,1], k = 3))
print(number_of_subarrays(nums = [2,4,6], k = 1))
print(number_of_subarrays(nums = [2,2,2,1,2,2,1,2,2,2], k = 2))


