# Time: O(n log m); Space: O(1)
def count_negatives(grid):
    n, m = len(grid), len(grid[0])
    count = 0

    for i in range(n):
        low, high = 0, m - 1

        while low <= high:
            mid = low + (high - low) // 2

            if grid[i][mid] < 0:
                high = mid - 1
            else:
                low = mid + 1

        if low < n and grid[i][low] < 0:
            count += m - low

    return count


# Time: O(n + m); Space: O(1)
def count_negatives2(grid):
    n, m = len(grid), len(grid[0])
    row, col = 0, m - 1
    count = 0

    while row < n and col >= 0:
        if grid[row][col] < 0:
            count += n - row
            col -= 1
        else:
            row += 1

    return count


# Test cases:
print(count_negatives([[4, 3, 2, -1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]]))
