from collections import deque


def find_median(nums):
    nums = list(sorted(nums))

    if len(nums) % 2 != 0:
        return nums[len(nums) // 2]

    one = len(nums) // 2
    two = len(nums) // 2 + 1
    median = (one + two) / 2
    return median


# Time: O(n^n log n); Space: O(n)
def activity_notifications(expenditure, d):
    prior_activity = deque()
    count = 0

    for ex in expenditure:
        if len(prior_activity) < d:
            prior_activity.append(ex)
        else:
            median = find_median(prior_activity)
            if ex >= median * 2:
                count += 1
                prior_activity.popleft()
                prior_activity.append(ex)

    return count


def find_median2(counter, d):
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


def activity_notifications2(expenditure, d):
    counter = [0] * (max(expenditure) + 1)
    prior_activity = deque()
    for i in range(d):
        prior_activity.append(expenditure[i])
        counter[expenditure[i]] += 1

    res = 0
    for ex in expenditure[d:]:
        median = find_median2(counter, d)
        if ex >= median * 2:
            res += 1

        el_to_remove = prior_activity.popleft()
        counter[el_to_remove] -= 1
        prior_activity.append(ex)
        counter[ex] += 1

    return res


# Test cases:
print(activity_notifications2([1, 2, 3, 4, 5], 2))
print(activity_notifications2([2, 3, 4, 2, 3, 6, 8, 4, 5], 5))
print(activity_notifications2([1, 2, 3, 4, 4], 4))
