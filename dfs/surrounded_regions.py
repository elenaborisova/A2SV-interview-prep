# Time: O(r * c); Space: O(r * c)
def solve(board):
    ROWS, COLS = len(board), len(board[0])

    def capture(r, c):
        if (not 0 <= r < ROWS) or (not 0 <= c < COLS) or board[r][c] != 'O':
            return

        board[r][c] = 'T'
        capture(r + 1, c)
        capture(r - 1, c)
        capture(r, c + 1)
        capture(r, c - 1)

    # 1. (DFS) Capture unsurrounded regions (O -> T)
    for r in range(ROWS):
        for c in range(COLS):
            # only the borders of the grid
            if board[r][c] == 'O' and (r in [0, ROWS - 1] or c in [0, COLS - 1]):
                capture(r, c)

    # 2. Capture surrounded regions (O -> X) / Uncapture unsurrounded regions (T -> O)
    for r in range(ROWS):
        for c in range(COLS):
            if board[r][c] == 'O':
                board[r][c] = 'X'
            elif board[r][c] == 'T':
                board[r][c] = 'O'
