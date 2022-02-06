from collections import Counter


# Time: O(n); Space: O(n)
def remove_duplicate_letters(s):
    counter = Counter(s)
    stack = []
    visited = set()

    for char in s:
        counter[char] -= 1

        if char not in stack:
            while stack and ord(stack[-1]) > ord(char) and counter[stack[-1]] > 0:
                visited.remove(stack.pop())

            stack.append(char)
            visited.add(char)

    return ''.join(stack)


# Test cases:
print(remove_duplicate_letters('bcabc'))
print(remove_duplicate_letters('cbacdcbc'))
print(remove_duplicate_letters('bbcaac'))
print(remove_duplicate_letters('bbbacacca'))
