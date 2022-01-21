import heapq


# Time: O(n log k); Space: O(k)
def kth_largest_number(nums, k):
    h = []

    for n in nums:
        heapq.heappush(h, int(n))

        if len(h) > k:
            heapq.heappop(h)

    return str(h[0])


# Quick Select; Worst case time O(n^2); Space: O(n)
def kth_largest_number2(nums, k):
    nums = list(map(int, nums))
    k = len(nums) - k

    def quick_select(l, r):
        pivot, p = nums[r], l
        for i in range(l, r):
            if nums[i] <= pivot:
                nums[p], nums[i] = nums[i], nums[p]
                p += 1
        nums[p], nums[r] = nums[r], nums[p]

        if p > k:
            return quick_select(l, p - 1)
        elif p < k:
            return quick_select(p + 1, r)
        else:
            return nums[p]

    return str(quick_select(0, len(nums) - 1))


# Test cases:
print(kth_largest_number2(["3", "6", "7", "10"], 4))
print(kth_largest_number2(["2", "21", "12", "1"], 3))
print(kth_largest_number2(["0", "0"], 2))
print(kth_largest_number2([2, 21, 12, 1, 10, 0], 1))
