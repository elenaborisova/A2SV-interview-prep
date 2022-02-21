import collections


# Time: O(n); Space: O(n)
def length_of_longest_substring(s):
    counter = collections.defaultdict(int)
    longest = l = r = 0

    while r < len(s):
        counter[s[r]] += 1

        while counter[s[r]] > 1:
            counter[s[l]] -= 1
            l += 1

        longest = max(longest, r - l + 1)
        r += 1

    return longest


# Test cases:
print(length_of_longest_substring('abcabcbb'))
print(length_of_longest_substring('bbbbb'))
print(length_of_longest_substring('pwwkew'))
print(length_of_longest_substring('./  ./!'))
