# Time: O(n); Space: O(n)
def is_valid(s):
    d = {
        ')': '(',
        '}': '{',
        ']': '[',
    }
    stack = []

    for p in s:
        if p not in d:
            stack.append(p)
            continue

        if p in d and (not stack or d[p] != stack[-1]):
            return False
        else:
            stack.pop()

    return True if not stack else False


# Test cases:
print(is_valid('({[})'))
