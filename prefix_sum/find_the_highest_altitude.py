# Time: O(n); Space: O(1)
def largest_altitude(gain):
    highest = 0
    cur_sum = 0

    for g in gain:
        cur_sum += g
        highest = max(highest, cur_sum)

    return highest


# Test cases:
print(largest_altitude([-5, 1, 5, 0, -7]))
print(largest_altitude([-4, -3, -2, -1, 4, 3, 2]))
