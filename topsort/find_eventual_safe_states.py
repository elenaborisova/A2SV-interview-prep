# DFS
def eventual_safe_nodes(graph):
    def explore(i):
        visited[i] = 'visited'

        for v in graph[i]:
            if visited[v] == 'visited' or (visited[v] == 'unvisited' and explore(v)):
                return True

        visited[i] = 'safe'
        res.append(i)
        return False

    visited = ['unvisited'] * len(graph)
    res = []

    for i in range(len(graph)):
        if visited[i] == 'unvisited':
            explore(i)

    return sorted(res)


# Test cases:
print(eventual_safe_nodes([[1, 2], [2, 3], [5], [0], [5], [], []]))
