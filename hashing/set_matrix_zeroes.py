# Time: O(n * m); Space: O(1)
def set_zeroes(matrix):
    is_first_row_zero = False
    is_first_col_zero = False

    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            if matrix[r][c] == 0:
                matrix[r][0] = 0
                matrix[0][c] = 0

                if r == 0:
                    is_first_row_zero = True
                if c == 0:
                    is_first_col_zero = True

    for r in range(1, len(matrix)):
        for c in range(1, len(matrix[0])):
            if matrix[r][0] == 0:
                matrix[r][c] = 0

            if matrix[0][c] == 0:
                matrix[r][c] = 0

    if is_first_row_zero:
        for c in range(len(matrix[0])):
            matrix[0][c] = 0

    if is_first_col_zero:
        for r in range(len(matrix)):
            matrix[r][0] = 0

    return matrix


# Test cases:
print(set_zeroes([[1, 1, 1], [1, 0, 1], [1, 1, 1]]))
print(set_zeroes([[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]))
