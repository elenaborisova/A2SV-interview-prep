from collections import deque


class RecentCounter:

    def __init__(self):
        self.counter = deque()

    # Time: O(3000) == O(1); Space: O(3000) == O(1)
    def ping(self, t: int) -> int:
        self.counter.append(t)

        while self.counter[0] < t - 3000:
            self.counter.popleft()

        return len(self.counter)


# Test cases:
recentCounter = RecentCounter()
print(recentCounter.ping(1))     # requests = [1], range is [-2999, 1], return 1
print(recentCounter.ping(100))   # requests = [1, 100], range is [-2900, 100], return 2
print(recentCounter.ping(3001))  # requests = [1, 100, 3001], range is [1, 3001], return 3
print(recentCounter.ping(3002))  # requests = [1, 100, 3001, 3002], range is [2, 3002], return 3
