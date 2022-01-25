import math


def theatre_square(n, m, a):
    n_side = math.ceil(n / a)
    m_side = math.ceil(m / a)

    return n_side * m_side


# Test cases:
# m, n, a = list(map(int, input().split()))
# print(theatre_square(m, n, a))
print(theatre_square(6, 9, 4))
