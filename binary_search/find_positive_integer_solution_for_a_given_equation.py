"""
   This is the custom function interface.
   You should not implement it, or speculate about its implementation
   class CustomFunction:
       # Returns f(x, y) for any given positive integers x and y.
       # Note that f(x, y) is increasing with respect to both x and y.
       # i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
       def f(self, x, y):

"""


# Time: O(x log y); Space: O()
def find_solution(customfunction, z):
    res = []

    for x in range(1, 1001):
        low, high = 1, 1001

        while low <= high:
            y = low + (high - low) // 2

            if customfunction.f(x, y) == z:
                res.append([x, y])
                break
            elif customfunction.f(x, y) > z:
                high = y - 1
            else:
                low = y + 1

    return res
