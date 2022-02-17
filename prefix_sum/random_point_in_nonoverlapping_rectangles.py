import random
from typing import List


class Solution:

    def __init__(self, rects: List[List[int]]):
        self.rects = rects
        self.distribution = self.calculate_distribution()

    def calculate_distribution(self):
        areas = []
        for rect in self.rects:
            area = abs(rect[0] - rect[2] + 1) * abs(rect[1] - rect[3] + 1)
            areas.append(area)

        d = []
        total_area = sum(areas)
        for area in areas:
            d.append(area / total_area)

        return d

    def pick(self) -> List[int]:
        random_rect = random.choices(population=self.rects, k=1, weights=self.distribution)[0]
        x = random.randrange(min(random_rect[0], random_rect[2]), max(random_rect[0], random_rect[2]))
        y = random.randrange(min(random_rect[1], random_rect[3]), max(random_rect[1], random_rect[3]))
        return [x, y]


# Test cases:
obj = Solution([[-2, -2, 1, 1], [2, 2, 4, 6]])
print(obj.pick())
