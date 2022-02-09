def superDigit(n, k):
    if len(n) == 1:
        return int(n)

    cur_sum = 0
    for d in n:
        cur_sum += int(d)
    cur_sum *= k

    return superDigit(str(cur_sum), 1)


# Test cases:
print(superDigit('123', 3))
print(superDigit('148', 3))
print(superDigit('9875', 4))
