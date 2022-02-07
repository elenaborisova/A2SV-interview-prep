from collections import deque, Counter


# Time: O(n^2); Space: O(n)
def count_students(students, sandwiches):
    students = deque(students)  # queue
    sandwiches.reverse()  # stack

    while students:
        if students[0] == sandwiches[-1]:
            students.popleft()
            sandwiches.pop()
        else:
            students.append(students.popleft())

            if sum(students) == 0 or sum(students) == len(students):
                break

    return len(students)


# Time: O(n); Space: O(n)
def count_students2(students, sandwiches):
    students = Counter(students)

    for sandwich in sandwiches:
        if not students[sandwich]:
            break
        students[sandwich] -= 1

    return sum(students.values())


# Test cases:
print(count_students(students=[1, 1, 1, 0, 0, 1], sandwiches=[1, 0, 0, 0, 1, 1]))
print(count_students(students=[1, 1, 0, 0], sandwiches=[0, 1, 0, 1]))
