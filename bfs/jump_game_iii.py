from collections import deque


# Time: O(n); Space: O(n)
def can_reach(arr, start):
    queue = deque([start])
    seen = set()

    while queue:
        i = queue.popleft()
        seen.add(i)

        if arr[i] == 0:
            return True

        if 0 <= i + arr[i] < len(arr) and i + arr[i] not in seen:
            queue.append(i + arr[i])
        if 0 <= i - arr[i] < len(arr) and i - arr[i] not in seen:
            queue.append(i - arr[i])

    return False


# Test cases:
print(can_reach(arr=[4, 2, 3, 0, 3, 1, 2], start=5))
print(can_reach(arr=[4, 2, 3, 0, 3, 1, 2], start=0))
print(can_reach(arr=[3, 0, 2, 1, 2], start=2))
