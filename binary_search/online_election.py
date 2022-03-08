import collections


class TopVotedCandidate:

    def __init__(self, persons, times):
        self.leads = []
        self.times = times
        count = collections.defaultdict(int)
        lead = -1

        for p in persons:
            count[p] += 1
            if count[p] >= count.get(lead, 0):
                lead = p
            self.leads.append(lead)

    def find_time(self, t):
        low, high = 0, len(self.times) - 1

        while low <= high:
            mid = low + (high - low) // 2

            if self.times[mid] == t:
                return mid
            elif self.times[mid] < t:
                low = mid + 1
            else:
                high = mid - 1

        return high

    def q(self, t):
        pos = self.find_time(t)
        return self.leads[pos]


# Your TopVotedCandidate object will be instantiated and called as such:
obj = TopVotedCandidate([0, 1, 1, 0, 0, 1, 0], [0, 5, 10, 15, 20, 25, 30])
print(obj.q(15))
print(obj.q(24))
print(obj.q(8))
print(obj.q(25))
print(obj.q(12))
print(obj.q(3))
