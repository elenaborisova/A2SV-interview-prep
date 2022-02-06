# Time: O(n log n); Space: O(n)
def number_of_weak_characters(properties):
    properties.sort(key=lambda x: (-x[0], x[1]))
    count, stack = 0, []

    for pair in properties:
        if not stack:
            stack.append(pair)
        elif pair[0] < stack[-1][0] and pair[1] < stack[-1][1]:
            count += 1
        elif pair[1] > stack[-1][1]:
            stack.pop()
            stack.append(pair)

    return count


# Test cases:
print(number_of_weak_characters([[5, 5], [6, 3], [3, 6]]))
print(number_of_weak_characters([[2, 2], [3, 3]]))
print(number_of_weak_characters([[1, 5], [10, 4], [4, 3]]))
print(number_of_weak_characters([[1, 1], [2, 1], [2, 2], [1, 2]]))
print(number_of_weak_characters([[7, 9], [10, 7], [6, 9], [10, 4], [7, 5], [7, 10]]))
print(number_of_weak_characters([[10, 1], [5, 1], [7, 10], [4, 1], [5, 9], [6, 9], [7, 2], [1, 10]]))
