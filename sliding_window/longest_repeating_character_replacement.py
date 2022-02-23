import collections


# Time: O(n); Space: O(n)
def character_replacement(s, k):
    d = collections.defaultdict(int)
    max_len = 1

    l, r = 0, 0
    while r < len(s):
        d[s[r]] += 1

        if len(d) > k + 1 or sum(d.values()) - max(d.values()) > k:
            d[s[l]] -= 1
            if d[s[l]] == 0: del d[s[l]]
            l += 1

        max_len = max(max_len, r - l + 1)
        r += 1

    return max_len


# Test cases:
print(character_replacement('BABA', k=0))
print(character_replacement('A', k=0))
print(character_replacement("AABABBA", k=1))
