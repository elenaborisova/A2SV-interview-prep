from collections import deque, defaultdict


# BFS; Time: O(n + prerequisites)
def can_finish(num_courses, prerequisites):
    dependencies = [0] * num_courses
    outgoing = defaultdict(set)

    for course, pre in prerequisites:
        outgoing[pre].add(course)
        dependencies[course] += 1

    queue = deque()
    for course in range(num_courses):
        if dependencies[course] == 0:
            queue.append(course)

    count = 0
    while queue:
        course = queue.popleft()
        count += 1

        for dep in outgoing[course]:
            dependencies[dep] -= 1
            if dependencies[dep] == 0:
                queue.append(dep)

    return count == num_courses


# DFS
def can_finish2(num_courses, prerequisites):
    dependencies = {i: [] for i in range(num_courses)}

    for course, pre in prerequisites:
        dependencies[course].append(pre)

    visited = set()

    def dfs(course):
        # loop detected
        if course in visited:
            return False
        if not dependencies[course]:
            return True

        visited.add(course)
        for pre in dependencies[course]:
            if not dfs(pre):
                return False

        visited.remove(course)
        dependencies[course] = []
        return True

    for course in range(num_courses):
        if not dfs(course):
            return False
    return True
