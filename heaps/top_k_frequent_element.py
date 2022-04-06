import heapq
from collections import Counter


# Time: O(n log k); Space: O(n + k)
def top_k_frequent(nums, k):
    counter = Counter(nums)
    heap = []

    for n, c in counter.items():
        heapq.heappush(heap, (c, n))

        if len(heap) > k:
            heapq.heappop(heap)

    return [x[1] for x in heap]


# Test cases:
print(top_k_frequent(nums=[1, 1, 1, 2, 2, 3], k=2))
print(top_k_frequent(nums=[1], k=1))
