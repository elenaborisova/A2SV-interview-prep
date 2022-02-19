def longest_ones(nums, k):
    longest = flip_count = l = r = 0

    while r < len(nums):
        if nums[r] == 0:
            if flip_count == k:
                while nums[l] == 1:
                    l += 1
                l += 1
            else:
                flip_count += 1

        longest = max(longest, r - l + 1)
        r += 1

    return longest


print(longest_ones(nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2))
