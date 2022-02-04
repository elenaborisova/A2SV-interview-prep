# Time: O(n log n); Space: O(n)
def car_fleet(target, position, speed):
    pair = sorted(zip(position, speed), reverse=True)
    stack = []

    for pos, v in pair:

        dist = target - pos
        time = dist / v

        if not stack:
            stack.append(time)
        elif time > stack[-1]:
            stack.append(time)

    return len(stack)


# Test cases:
print(car_fleet(target=12, position=[10, 8, 0, 5, 3], speed=[2, 4, 1, 1, 3]))
