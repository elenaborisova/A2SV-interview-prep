# Time: O(n); Space: O(1)
def is_isomorphic(s, t):
    mapping = {}
    mapped = set()

    for i in range(len(s)):
        if t[i] in mapping and mapping[t[i]] != s[i]:
            return False

        if s[i] in mapped and t[i] not in mapping:
            return False

        mapping[t[i]] = s[i]
        mapped.add(s[i])

    return True


# Test cases:
print(is_isomorphic(s="egg", t="add"))
print(is_isomorphic(s="foo", t="bar"))
print(is_isomorphic(s="paper", t="title"))
print(is_isomorphic(s="badc", t="baba"))
print(is_isomorphic(s="bg", t="gb"))
