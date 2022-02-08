from collections import Counter, deque


def predict_party_victory(senate):
    counter = Counter(senate)
    senate = deque(senate)
    blocked = deque()

    while counter['R'] and counter['D']:

        if senate[0] == 'R':
            if blocked and blocked[0] == 'R':
                blocked.popleft()
                senate.popleft()
                counter['R'] -= 1
            else:
                blocked.append('D')
                senate.append(senate.popleft())

        elif senate[0] == 'D':
            if blocked and blocked[0] == 'D':
                blocked.popleft()
                senate.popleft()
                counter['D'] -= 1
            else:
                blocked.append('R')
                senate.append(senate.popleft())

    return 'Radiant' if counter['R'] else 'Dire'


# Better Implementation
def predict_party_victory2(senate):
    R = deque(i for i, x in enumerate(senate) if x == 'R')  # keep indices of all R
    D = deque(i for i, x in enumerate(senate) if x == 'D')  # keep indices of all D

    while R and D:
        r, d = R.popleft(), D.popleft()
        if r < d:
            R += r + len(senate)
        else:
            D += d + len(senate)

    return R and 'Radiant' or 'Dire'


# Test cases:
print(predict_party_victory('RD'))
print(predict_party_victory('DDRRR'))
