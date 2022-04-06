import heapq


class KthLargest:

    def __init__(self, k, nums):
        self.k = k
        self.nums = nums
        heapq.heapify(self.nums)  # O(n)

    # Time: O((m + n) log k); Space: O(k) where m is the number of calls to add()
    def add(self, val):
        heapq.heappush(self.nums, val)  # O(log k)

        while len(self.nums) > self.k:
            heapq.heappop(self.nums)

        return self.nums[0]


# Test cases:
obj = KthLargest(3, [4, 5, 8, 2])
print(obj.add(3))
print(obj.add(5))
print(obj.add(10))
print(obj.add(9))
print(obj.add(4))
