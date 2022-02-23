import collections


# Time: O(n); Space: O(n)
def find_repeated_dna_sequences(s):
    freq = collections.defaultdict(int)
    res = set()

    l, r = 0, 9
    while r < len(s):
        substring = s[l:r + 1]
        freq[substring] += 1

        if freq[substring] > 1:
            res.add(substring)

        l += 1
        r += 1

    return list(res)


# Test cases:
print(find_repeated_dna_sequences('AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT'))
print(find_repeated_dna_sequences('AAAAAAAAAAAAA'))
print(find_repeated_dna_sequences("AAAAAAAAAAA"))
