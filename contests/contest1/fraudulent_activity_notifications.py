from collections import deque


def find_median(nums):
    nums = list(sorted(nums))

    if len(nums) % 2 != 0:
        return nums[len(nums) // 2]

    one = len(nums) // 2
    two = len(nums) // 2 + 1
    median = (one + two) / 2
    return median


def activityNotifications(expenditure, d):
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
