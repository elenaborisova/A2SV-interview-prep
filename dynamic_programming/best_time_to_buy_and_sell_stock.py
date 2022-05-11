# Time: O(n); Space: O(1)
def max_profit(prices):
    buy_price = prices[0]
    max_p = 0

    for i in range(1, len(prices)):
        if prices[i] <= buy_price:
            buy_price = prices[i]
        else:
            max_p = max(max_p, prices[i] - buy_price)

    return max_p


# Test cases:
print(max_profit([7, 1, 5, 3, 6, 4]))
print(max_profit([1, 2, 3, 4, 5]))
