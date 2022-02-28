# Time: O(n); Space: O(1)
def int_to_roman(num):
    d = {
        1000: 'M',
        900: 'CM',
        500: 'D',
        400: 'CD',
        100: 'C',
        90: 'XC',
        50: 'L',
        40: 'XL',
        10: 'X',
        9: 'IX',
        5: 'V',
        4: 'IV',
        1: 'I',
    }

    res = []

    for i in d:
        res.append((num // i) * d[i])
        num %= i

    return ''.join(res)


# Test cases:
print(int_to_roman(58))
print(int_to_roman(3))
