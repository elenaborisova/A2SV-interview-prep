# Time: O(n * m); Space: O(1)
def minimum_total(triangle):
    n = len(triangle)

    for r in range(n - 2, -1, -1):
        for c in range(r + 1):
            triangle[r][c] += min(triangle[r + 1][c], triangle[r + 1][c + 1])

    return triangle[0][0]


# Test cases:
print(minimum_total([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]))
