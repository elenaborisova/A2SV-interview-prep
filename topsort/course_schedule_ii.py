from collections import defaultdict, deque


def find_order(num_courses, prerequisites):
    dependencies = [0] * num_courses
    outgoing = defaultdict(set)

    for course, pre in prerequisites:
        outgoing[pre].add(course)
        dependencies[course] += 1

    queue = deque()
    for course in range(num_courses):
        if dependencies[course] == 0:
            queue.append(course)

    res = []
    while queue:
        course = queue.popleft()
        res.append(course)

        for dep in outgoing[course]:
            dependencies[dep] -= 1
            if dependencies[dep] == 0:
                queue.append(dep)

    return res if len(res) == num_courses else []
