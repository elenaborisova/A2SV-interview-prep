from collections import deque


def find_median(counter, d):
    is_odd = False if d % 2 == 0 else True
    c, one, two = 0, 0, 0

    for i, freq in enumerate(counter):
        c += freq

        if is_odd and c >= d // 2 + 1:
            one = two = i
            break

        if not is_odd and not one and c >= d // 2:
            one = i
        if not is_odd and c >= d // 2 + 1:
            two = i
            break

    return (one + two) / 2


def activity_notifications(expenditure, d):
    counter = [0] * (max(expenditure) + 1)
    prior_activity = deque()
    for i in range(d):
        prior_activity.append(expenditure[i])
        counter[expenditure[i]] += 1

    res = 0
    for ex in expenditure[d:]:
        median = find_median(counter, d)
        if ex >= median * 2:
            res += 1

        el_to_remove = prior_activity.popleft()
        counter[el_to_remove] -= 1
        prior_activity.append(ex)
        counter[ex] += 1

    return res


# Test cases:
print(activity_notifications([1, 2, 3, 4, 5], 2))
print(activity_notifications([2, 3, 4, 2, 3, 6, 8, 4, 5], 5))
print(activity_notifications([1, 2, 3, 4, 4], 4))
