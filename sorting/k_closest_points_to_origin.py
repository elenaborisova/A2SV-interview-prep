import math
import heapq


# Time: O(n * log n); Space: O(n)
# MinHeap
def k_closest(points, k):
    distances = {}  # O(n) space
    h = []  # O(n) space

    for point in points:
        distance = math.sqrt(point[0] ** 2 + point[1] ** 2)

        if distance not in distances:
            distances[distance] = []
        distances[distance].append(point)

        heapq.heappush(h, distance)  # O(log n) time

    res = []  # O(k) space
    for _ in range(k):  # O(k) time
        smallest = heapq.heappop(h)  # O(log n) time
        res.append(distances[smallest][-1])
        distances[smallest].pop()

    return res


# MaxHeap; Optimized
# Time: O(n log k); Space: O(k)
def k_closest2(points, k):
    h = []  # O(k) space

    for point in points:  # O(n) time
        distance = math.sqrt(point[0] ** 2 + point[1] ** 2)
        heapq.heappush(h, (distance * -1, point))  # O(log k) time

        if len(h) > k:
            heapq.heappop(h)  # O(log k) time

    res = []  # O(k) space
    for distance, point in h:  # O(k) time
        res.append(point)

    return res


# Test cases:
print(k_closest2([[1, 3], [-2, 2]], 1))
print(k_closest2([[3, 3], [5, -1], [-2, 4]], 2))
print(k_closest2([[0, 1], [1, 0]], 2))
