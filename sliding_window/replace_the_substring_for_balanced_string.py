import collections


# Time: O(n); Space: O(1)
def balanced_string(s):
    count = collections.Counter(s)
    res = n = len(s)

    l = r = 0
    while r < n:
        count[s[r]] -= 1

        while l < n and max(count['Q'], count['W'], count['E'], count['R']) <= n / 4:
            res = min(res, r - l + 1)
            count[s[l]] += 1
            l += 1

        r += 1

    return res


# Test cases:
print(balanced_string('QWER'))
print(balanced_string('QQWE'))
print(balanced_string('QQQW'))
print(balanced_string('QQQQ'))
print(balanced_string('WQWRQQQW'))
