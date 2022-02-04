# Brute force; Time: O(n); Space: ?? a lot
def decode_at_index(s, k):
    decoded = ''

    for char in s:
        if char.isalpha():
            decoded += char
        else:
            decoded += decoded * (int(char) - 1)

    return decoded[k - 1]


# Time: O(n); Space: O(1)
def decode_at_index2(s, k):
    size = 0
    for c in s:
        if c.isdigit():
            size *= int(c)
        else:
            size += 1

    for c in reversed(s):
        k %= size
        if k == 0 and c.isalpha():
            return c

        if c.isdigit():
            size /= int(c)
        else:
            size -= 1


# Test cases:
print(decode_at_index2(s="leet2code3", k=10))
print(decode_at_index2(s="ha22", k=5))
print(decode_at_index(s="a2345678999999999999999", k=1))
