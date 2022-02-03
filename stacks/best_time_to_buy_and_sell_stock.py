# Time: O(n); Space: O(n)
def max_profit(prices):
    stack = []
    max_p = 0

    for p in prices:
        if not stack:
            stack.append(p)
        else:
            if p < stack[-1]:
                stack.pop()
                stack.append(p)
            else:
                max_p = max(max_p, p - stack[-1])

    return max_p


# Test cases:
print(max_profit([7, 1, 5, 3, 6, 4]))
print(max_profit([7, 6, 4, 3, 1]))
