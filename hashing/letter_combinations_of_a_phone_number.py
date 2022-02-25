def letter_combinations(digits):
    digits_to_letters = {
        '2': ['a', 'b', 'c'],
        '3': ['d', 'e', 'f'],
        '4': ['g', 'h', 'i'],
        '5': ['j', 'k', 'l'],
        '6': ['m', 'n', 'o'],
        '7': ['p', 'q', 'r', 's'],
        '8': ['t', 'u', 'v'],
        '9': ['w', 'x', 'y', 'z'],
        ' ': [''],
    }
    digits += ' ' * (4 - len(digits))
    res = []

    for l1 in digits_to_letters[digits[0]]:
        for l2 in digits_to_letters[digits[1]]:
            for l3 in digits_to_letters[digits[2]]:
                for l4 in digits_to_letters[digits[3]]:
                    comb = l1 + l2 + l3 + l4
                    if comb != '':
                        res.append(comb)

    return res


# Much better implementation
def letter_combinations2(digits):
    if not digits:
        return []

    digit_map = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno',
                 '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
    res = ['']

    for i in range(len(digits)):
        res = [prev + l for prev in res for l in digit_map[digits[i]]]

    return res


# Test cases:
print(letter_combinations2('23'))
print(letter_combinations2(''))
