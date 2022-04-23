# Time: O(r * c); Space: O(r * c)
def num_enclaves(grid):
    ROWS, COLS = len(grid), len(grid[0])

    def dfs(r, c):
        if (not 0 <= r < ROWS) or (not 0 <= c < COLS) or grid[r][c] != 1:
            return

        grid[r][c] = -1
        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)

    for r in range(ROWS):
        for c in range(COLS):
            if (r in [0, ROWS - 1] or c in [0, COLS - 1]) and grid[r][c] == 1:
                dfs(r, c)

    # count the remaining 1s
    count = 0
    for r in range(ROWS):
        for c in range(COLS):
            if grid[r][c] == 1:
                count += 1

    return count


# Test cases:
print(num_enclaves([[0, 0, 0, 0], [1, 0, 1, 0], [0, 1, 1, 0], [0, 0, 0, 0]]))
print(num_enclaves([[0, 1, 1, 0], [0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 0, 0]]))
