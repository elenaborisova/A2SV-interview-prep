import collections


# Recursion; Time: O(n log n)
def longest_nice_substring(s):
    if len(s) == 0:
        return ''

    d = collections.Counter(s)

    for i, char in enumerate(s):
        if (char.isupper() and char.lower() not in d) \
                or (char.islower() and char.upper() not in d):

            one = longest_nice_substring(s[:i])
            two = longest_nice_substring(s[i + 1:])
            if len(one) >= len(two):
                return one
            else:
                return two

    return s


# Better implementation
def longest_nice_substring2(s):
    if not s:
        return ''

    ss = set(s)

    for i, c in enumerate(s):
        if c.swapcase() not in ss:
            s1 = longest_nice_substring2(s[:i])
            s2 = longest_nice_substring2(s[i + 1:])
            return max(s1, s2, key=len)

    return s


# Iterative approach; Time: O(n^2); Space: O(n)
def longest_nice_substring3(s):
    longest = ''

    for i in range(len(s)):
        for j in range(i + 1, len(s)):
            substring = s[i:j + 1]
            if set(substring) == set(substring.swapcase()):
                longest = max(longest, substring, key=len)

    return longest


# Test cases:
print(longest_nice_substring3('YazaAay'))
