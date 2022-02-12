from collections import deque


# Time: O(n); Space: O(n)
def shortest_subarray(nums, k):
    queue = deque([(0, 0)])
    res = len(nums) + 1
    cur_sum = 0

    for i, n in enumerate(nums):
        cur_sum += n

        while queue and cur_sum - queue[0][1] >= k:
            res = min(res, i - queue[0][0] + 1)
            queue.popleft()

        while queue and cur_sum <= queue[-1][1]:
            queue.pop()

        queue.append((i + 1, cur_sum))

    return res if res < len(nums) + 1 else -1


# Test cases:
print(shortest_subarray([1], 1))
print(shortest_subarray([1, 2], 4))
print(shortest_subarray([2, -1, 2], 3))
print(shortest_subarray([17, 85, 93, -45, -21], 150))
print(shortest_subarray([84, -37, 32, 40, 95], 167))
print(shortest_subarray([75, -32, 50, 32, 97, 45, 324, 2, -10], 129))
