import collections


# Time: O(n); Space: O(1)
def total_fruit(fruits):
    basket = collections.defaultdict(int)
    one = two = -1
    res = l = r = 0

    while r < len(fruits):
        if one < 0 and fruits[r] != two:
            one, two = two, fruits[r]

        elif fruits[r] != one and fruits[r] != two:
            res = max(res, r - l)
            while basket[one] and basket[two]:
                basket[fruits[l]] -= 1
                l += 1

            one = one if basket[one] else two
            two = fruits[r]

        basket[fruits[r]] += 1
        r += 1

    return max(res, r - l)


# Better implementation
def total_fruit2(fruits):
    basket = collections.defaultdict(int)
    res = l = r = 0

    while r < len(fruits):
        basket[fruits[r]] += 1

        while len(basket) > 2:
            basket[fruits[l]] -= 1
            if not basket[fruits[l]]:
                basket.pop(fruits[l])
            l += 1

        res = max(res, r - l + 1)
        r += 1

    return res


# Test cases:
print(total_fruit2([1, 2, 3, 2, 2]))
print(total_fruit2([1, 2, 1]))
print(total_fruit2([0, 1, 2, 2]))
print(total_fruit2([4, 0, 1, 2, 3, 3, 3, 3, 4, 4]))
print(total_fruit2([3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4]))
print(total_fruit2([1, 0, 1, 4, 1, 4, 1, 2, 3]))
print(total_fruit2([0, 0, 1, 1]))
