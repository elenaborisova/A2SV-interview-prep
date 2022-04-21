# Time: O(n * n); Space: O(n)
def find_circle_num(is_connected):
    n = len(is_connected)
    seen = set()

    def dfs(i):
        for j, adj in enumerate(is_connected[i]):
            if adj == 1 and j not in seen:
                seen.add(j)
                dfs(j)

    count = 0

    for i in range(n):
        if i not in seen:
            dfs(i)
            count += 1

    return count


# Test cases:
print(find_circle_num([[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
