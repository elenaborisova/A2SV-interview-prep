from collections import deque


def oranges_rotting(grid):
    queue = deque()
    minutes = 0
    fresh_oranges = 0
    directions = {
        'up': (-1, 0),
        'down': (1, 0),
        'left': (0, -1),
        'right': (0, 1),
    }

    # Get initial rotten and fresh oranges
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == 2:
                queue.append([r, c])
            elif grid[r][c] == 1:
                fresh_oranges += 1

    while queue:

        for _ in range(len(queue)):
            row, col = queue.popleft()

            for d in directions:
                new_row = row + directions[d][0]
                new_col = col + directions[d][1]

                # Validate row and col
                if 0 <= new_row < len(grid) and 0 <= new_col < len(grid[0]) and grid[new_row][new_col] == 1:
                    grid[new_row][new_col] = 2
                    fresh_oranges -= 1
                    queue.append([new_row, new_col])

        minutes += 1

    return max(0, minutes - 1) if not fresh_oranges else -1


# Test cases:
print(oranges_rotting([[2, 1, 1], [1, 1, 0], [0, 1, 1]]))
print(oranges_rotting([[2, 1, 1], [0, 1, 1], [1, 0, 1]]))
print(oranges_rotting([[0, 2]]))
