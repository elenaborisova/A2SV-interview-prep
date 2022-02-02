from collections import defaultdict


# Time: O(n^2); Space: O(n^2)
def is_valid_sudoku(board):
    rows = defaultdict(set)
    cols = defaultdict(set)

    for x in range(0, 9, 3):
        for y in range(0, 9, 3):
            box = set()

            for i in range(y, y + 3):
                for j in range(x, x + 3):
                    cell = board[i][j]

                    if cell == '.':
                        continue

                    if cell in rows[i]:
                        return False
                    rows[i].add(cell)

                    if cell in cols[j]:
                        return False
                    cols[j].add(cell)

                    if cell in box:
                        return False
                    box.add(cell)

    return True


# Better implementation
def is_valid_sudoku2(board):
    rows = defaultdict(set)
    cols = defaultdict(set)
    boxes = defaultdict(set)

    for r in range(9):
        for c in range(9):
            if board[r][c] == '.':
                continue

            if board[r][c] in rows[r]:
                return False

            if board[r][c] in cols[c]:
                return False

            if board[r][c] in boxes[(r // 3, c // 3)]:
                return False

            rows[r].add(board[r][c])
            cols[c].add(board[r][c])
            boxes[(r // 3, c // 3)].add(board[r][c])

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
