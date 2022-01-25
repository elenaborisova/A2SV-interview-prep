# Time: O(n log n); Space: O(n)
def merge(intervals):
    intervals.sort()
    merged = []

    for i in range(1, len(intervals)):
        if intervals[i][0] <= intervals[i - 1][1]:
            intervals[i] = [intervals[i - 1][0], max(intervals[i - 1][1], intervals[i][1])]
        else:
            merged.append(intervals[i - 1])
    merged.append(intervals[-1])

    return merged


def merge2(intervals):
    intervals.sort()
    merged = []

    for interval in intervals:
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
        else:
            merged[-1][1] = max(merged[-1][1], interval[1])

    return merged


# Test cases:
print(merge([[1, 3], [2, 6], [8, 10], [15, 18]]))
print(merge([[1, 4], [4, 5]]))
print(merge([[1, 4], [2, 3]]))
print(merge([[2, 3], [4, 5], [6, 7], [8, 9], [1, 10]]))
