# Time: O(n); Space: O(n)
def flood_fill(image, sr, sc, new_color):
    if image[sr][sc] == new_color:
        return image

    color = image[sr][sc]
    image[sr][sc] = new_color

    directions = {
        'up': (-1, 0),
        'down': (1, 0),
        'left': (0, -1),
        'right': (0, 1),
    }

    for d in directions:
        new_row = sr + directions[d][0]
        new_col = sc + directions[d][1]

        if 0 <= new_row < len(image) and 0 <= new_col < len(image[0]) and color == image[new_row][new_col]:
            flood_fill(image, new_row, new_col, new_color)
            image[new_row][new_col] = new_color

    return image


print(flood_fill(image=[[1, 1, 1], [1, 1, 0], [1, 0, 1]], sr=1, sc=1, new_color=2))
print(flood_fill(image = [[0,0,0],[0,0,0]], sr = 0, sc = 0, new_color = 2))
