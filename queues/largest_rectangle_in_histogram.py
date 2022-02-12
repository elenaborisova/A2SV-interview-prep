# Time: O(n); Space: O(n)
def largest_rectangle_area(heights):
    stack = []
    res = 0

    for i, h in enumerate(heights):
        start = i
        while stack and stack[-1][1] > h:
            index, height = stack.pop()
            res = max(res, height * (i - index))
            start = index
        stack.append((start, h))

    for i, h in stack:
        res = max(res, h * (len(heights) - i))

    return res


# Test cases:
print(largest_rectangle_area([2, 1, 5, 6, 2, 3]))
print(largest_rectangle_area([2, 4]))
print(largest_rectangle_area([1, 2, 3, 4, 5]))
