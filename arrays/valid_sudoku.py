from collections import defaultdict


# Time: O(n^2); Space: O(n^2)
def is_valid_sudoku(board):
    rows = defaultdict(list)
    cols = defaultdict(list)

    for x in range(0, 9, 3):
        for y in range(0, 9, 3):
            box = []

            for i in range(y, y + 3):
                for j in range(x, x + 3):
                    cell = board[i][j]

                    if cell == '.':
                        continue

                    if cell in rows[i]:
                        return False
                    rows[i].append(cell)

                    if cell in cols[j]:
                        return False
                    cols[j].append(cell)

                    if cell in box:
                        return False
                    box.append(cell)

    return True


# Test cases:
print(is_valid_sudoku([["5", "3", ".", ".", "7", ".", ".", ".", "."]
                          , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
                          , [".", "9", "8", ".", ".", ".", ".", "6", "."]
                          , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
                          , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
                          , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
                          , [".", "6", ".", ".", ".", ".", "2", "8", "."]
                          , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
                          , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]))
