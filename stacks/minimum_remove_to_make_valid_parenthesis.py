# Time: O(n); Space: O(n)
def min_remove_to_make_valid(s):
    stack = []
    open_count = 0

    for c in s:
        if c == ')' and not open_count:
            continue

        if c == '(':
            open_count += 1
        elif c == ')':
            open_count -= 1

        stack.append(c)

    closed_count = 0
    new_stack = []
    for c in stack[::-1]:
        if c == '(' and not closed_count:
            open_count -= 1
            continue

        if c == '(' and closed_count:
            closed_count -= 1
        elif c == ')':
            closed_count += 1

        new_stack.append(c)

    return ''.join(new_stack[::-1]) if open_count == closed_count else ''


# Time: O(n); Space: O(n)
def leetcode_solution(s):
    s = list(s)
    stack = []

    for i, char in enumerate(s):
        if char == '(':
            stack.append(i)
        elif char == ')':
            if stack:
                stack.pop()
            else:
                s[i] = ''

    while stack:
        s[stack.pop()] = ''

    return ''.join(s)


# Test cases:
print(min_remove_to_make_valid('lee(t(c)o)de)'))
print(min_remove_to_make_valid('a)b(c)d'))
print(min_remove_to_make_valid('))(('))
print(min_remove_to_make_valid('()(((('))
print(min_remove_to_make_valid('(a(b(c)d)'))
