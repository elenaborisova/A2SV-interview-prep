import heapq


# Time: O(n log n); Space: O(n)
def last_stone_weight(stones):
    stones = [s * -1 for s in stones]
    heapq.heapify(stones)

    while len(stones) > 1:
        x = heapq.heappop(stones) * -1
        y = heapq.heappop(stones) * -1

        if x != y:
            heapq.heappush(stones, (y - x))

    return stones[0] * -1 if stones else 0


# Test cases:
print(last_stone_weight([2, 7, 4, 1, 8, 1]))
print(last_stone_weight([1]))
