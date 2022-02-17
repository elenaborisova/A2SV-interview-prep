import random
from typing import List


class Solution:

    def __init__(self, w: List[int]):
        self.w = w
        self.distribution = self.calculateDistribution()
        self.indices = list(range(0, len(w)))

    def calculateDistribution(self):
        distribution = []
        total_sum = sum(self.w)

        for weight in self.w:
            distribution.append(weight / total_sum)

        return distribution

    def pickIndex(self) -> int:
        random_number = random.choices(self.indices, self.distribution)
        return random_number[0]
