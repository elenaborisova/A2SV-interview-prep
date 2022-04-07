import heapq


def furthest_building(heights, bricks, ladders):
    heap = []
    curr_sum = 0

    for i in range(len(heights) - 1):
        if heights[i] < heights[i + 1]:
            diff = heights[i + 1] - heights[i]
            heapq.heappush(heap, diff * -1)
            curr_sum += diff

        if curr_sum > bricks:
            if ladders:
                ladders -= 1
                curr_sum -= heapq.heappop(heap) * -1
            else:
                return i

    return len(heights) - 1


print(furthest_building(heights=[4, 2, 7, 6, 9, 14, 12], bricks=5, ladders=1))
print(furthest_building(heights=[4, 12, 2, 7, 3, 18, 20, 3, 19], bricks=10, ladders=2))
print(furthest_building(heights=[14, 3, 19, 3], bricks=17, ladders=0))
