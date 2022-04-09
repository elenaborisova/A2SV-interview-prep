from collections import deque


# DP; Time: O(amount * len(coins)); Space: O(amount)
def neetcode_solution(coins, amount):
    dp = [amount + 1] * (amount + 1)
    dp[0] = 0

    for a in range(1, amount + 1):
        for c in coins:
            if a - c >= 0:
                dp[a] = min(dp[a], 1 + dp[a - c])

    return dp[amount] if dp[amount] != amount + 1 else -1


# BFS
def leetcode_solution(coins, amount):
    queue = deque([(amount, 0)])
    visited = {amount}

    while queue:
        curr_amt, level = queue.popleft()
        if curr_amt == 0:
            return level

        for c in coins:
            new_amt = curr_amt - c
            if new_amt >= 0 and new_amt not in visited:
                queue.append((new_amt, level + 1))
                visited.add(new_amt)

    return -1


# Test cases:
print(leetcode_solution(coins=[1, 2, 5], amount=11))
print(leetcode_solution(coins=[1, 2, 5], amount=13))
print(leetcode_solution(coins=[2], amount=3))
print(leetcode_solution(coins=[1], amount=0))
