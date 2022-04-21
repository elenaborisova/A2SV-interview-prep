from typing import List


class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates


# Time: O(n); Space: O(n)
def get_importance(employees, id):
    employees_map = {empl.id: empl for empl in employees}

    def dfs(id):
        root = employees_map[id]
        total_importance = root.importance

        for subordinate_id in root.subordinates:
            total_importance += dfs(subordinate_id)

        return total_importance

    return dfs(id)


# Test cases:
root = Employee(1, 5, [2, 3])
empl1 = Employee(2, 3, [])
empl2 = Employee(3, 3, [])
print(get_importance([root, empl1, empl2], 1))
