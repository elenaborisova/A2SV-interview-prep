# Time: O(n^2); Space: O(1)
def time_required_to_buy(tickets, k):
    time = 0

    while tickets[k] > 0:
        for i, t in enumerate(tickets):
            if t > 0:
                time += 1
                tickets[i] -= 1

            if tickets[k] == 0:
                break

    return time


# Time: O(n); Space: O(1)
def time_required_to_buy2(tickets, k):
    time = tickets[k]  # it has to buy all at kth position

    for i in range(len(tickets)):
        if i < k:
            time += min(tickets[i], tickets[k])
            # for all pos before k it will exhaust all tickets or get till number till kth place

        elif i > k:
            time += min(tickets[i], tickets[k] - 1)
            # for all pos after k it can exhaust all tickets or get 1 less than the kth gets finished

    return time


# Test cases:
print(time_required_to_buy(tickets=[2, 3, 2], k=2))
print(time_required_to_buy(tickets=[5, 1, 1, 1], k=0))
