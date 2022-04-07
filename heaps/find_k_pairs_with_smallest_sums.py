import heapq


# Brute Force Solution; Time: O(n * m * log k); Space: O(k)
def k_smallest_pairs(nums1, nums2, k):
    heap = []

    for x in nums1:
        for y in nums2:
            val = (x + y) * -1
            heapq.heappush(heap, (val, [x, y]))

            if len(heap) > k:
                heapq.heappop(heap)

    heap.sort(key=lambda x: -x[0])
    return [x[1] for x in heap]


def leetcode_solution(nums1, nums2, k):
    heap = []

    for x in nums1:
        for y in nums2:
            if len(heap) < k:
                heapq.heappush(heap, (-x - y, [x, y]))
            else:
                if heap and -heap[0][0] > x + y:
                    heapq.heappop(heap)
                    heapq.heappush(heap, (-x - y, [x, y]))
                else:
                    break

    return [heapq.heappop(heap)[1] for _ in range(k) if heap]


# Time: O(k log k); Space: O(k)
def leetcode_solution2(nums1, nums2, k):
    res = []
    if not nums1 or not nums2 or not k:
        return res

    heap = []
    visited = set()

    heapq.heappush(heap, (nums1[0] + nums2[0], 0, 0))
    visited.add((0, 0))

    while len(res) < k and heap:
        _, i, j = heapq.heappop(heap)
        res.append([nums1[i], nums2[j]])

        if i + 1 < len(nums1) and (i + 1, j) not in visited:
            heapq.heappush(heap, (nums1[i + 1] + nums2[j], i + 1, j))
            visited.add((i + 1, j))

        if j + 1 < len(nums2) and (i, j + 1) not in visited:
            heapq.heappush(heap, (nums1[i] + nums2[j + 1], i, j + 1))
            visited.add((i, j + 1))

    return res





# Test cases:
print(k_smallest_pairs(nums1=[1, 7, 11], nums2=[2, 4, 6], k=3))
print(k_smallest_pairs(nums1=[1, 1, 2], nums2=[1, 2, 3], k=2))
print(k_smallest_pairs(nums1=[1, 2], nums2=[3], k=3))
