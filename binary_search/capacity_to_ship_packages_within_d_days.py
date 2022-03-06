# Time: O(n log n); Space: O(1)
def ship_within_days(weights, days):
    low = max(weights)
    high = sum(weights)
    min_capacity = high

    while low <= high:
        mid = low + (high - low) // 2

        cur_days, cur_daily_weight = 1, 0
        for w in weights:
            if cur_daily_weight + w > mid:
                cur_days += 1
                cur_daily_weight = w
            else:
                cur_daily_weight += w

        if cur_days <= days:
            min_capacity = min(min_capacity, mid)
            high = mid - 1
        else:
            low = mid + 1

    return min_capacity


# Test cases:
print(ship_within_days(weights=[3, 2, 2, 4, 1, 4], days=3))
print(ship_within_days(weights=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], days=5))
print(ship_within_days(weights=[1, 2, 3, 1, 1], days=4))
