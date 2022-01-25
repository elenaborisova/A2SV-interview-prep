import heapq


# MaxHeap, MinHeap; Time: O(n log n); Space: O(n)
def max_coins(piles):
    max_heap = [p * -1 for p in piles]
    heapq.heapify(max_heap)  # O(n)

    min_heap = [p for p in piles]
    heapq.heapify(min_heap)

    coins = 0
    for i in range(len(piles) // 3):  # O(n/3)
        heapq.heappop(max_heap)  # O(log n)
        coins += heapq.heappop(max_heap) * -1
        heapq.heappop(min_heap)

    return coins


# Time: O(n log n); O(1)
def max_coins2(piles):
    piles.sort()

    c = 0
    for x in range(len(piles) // 3, len(piles), 2):
        c += piles[x]

    return c


# Test cases:
print(max_coins([2, 4, 1, 2, 7, 8]))
print(max_coins([2, 4, 5]))
print(max_coins([9, 8, 7, 6, 5, 1, 2, 3, 4]))
