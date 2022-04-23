# Time: O(r * c); Space: (r * c)
def max_area_of_island(grid):
    def explore(grid, r, c):
        if (not 0 <= r < len(grid)) or (not (0 <= c < len(grid[0]))) or grid[r][c] == 0:
            return 0

        grid[r][c] = 0

        return 1 + explore(grid, r - 1, c) + explore(grid, r, c - 1) \
               + explore(grid, r + 1, c) + explore(grid, r, c + 1)

    max_area = 0

    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == 1:
                max_area = max(max_area, explore(grid, r, c))

    return max_area


# Test cases:
print(max_area_of_island([[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                          [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
                          [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]))
