from collections import deque


# Time: O(n); Space: O(n)
def longest_subarray(nums, limit):
    max_q, min_q = deque(), deque()
    res, l, r = 0, 0, 0

    while r < len(nums):
        while max_q and nums[r] > max_q[-1][1]:
            max_q.pop()
        while min_q and nums[r] < min_q[-1][1]:
            min_q.pop()

        max_q.append((r, nums[r]))
        min_q.append((r, nums[r]))

        while min_q and max_q and max_q[0][1] - min_q[0][1] > limit:
            l += 1
            if max_q[0][0] < l:
                max_q.popleft()
            if min_q[0][0] < l:
                min_q.popleft()

        res = max(res, r - l + 1)
        r += 1

    return res


# Test cases:
print(longest_subarray(nums=[8, 2, 4, 7], limit=4))
print(longest_subarray(nums=[10, 1, 2, 4, 7, 2], limit=5))
print(longest_subarray(nums=[4, 2, 2, 2, 4, 4, 2, 2], limit=0))
print(longest_subarray(nums=[1, 5, 6, 7, 8, 10, 6, 5, 6], limit=4))
