# Time: O(n); Space: O(n)
def daily_temperatures(temperatures):
    stack = []
    ans = [0] * len(temperatures)

    for day, temp in enumerate(temperatures):

        while stack and temperatures[stack[-1]] < temp:
            prev_day = stack.pop()
            ans[prev_day] = day - prev_day
        stack.append(day)

    return ans


# Looping backwards
def daily_temperatures2(temperatures):
    res = [0] * len(temperatures)
    stack = []

    for index in range(len(temperatures) - 1, -1, -1):

        while stack and temperatures[stack[-1]] <= temperatures[index]:
            stack.pop()

        res[index] = stack[-1] - index if stack else 0
        stack.append(index)

    return res


# Test cases:
print(daily_temperatures2([73, 74, 75, 71, 69, 72, 76, 73]))
