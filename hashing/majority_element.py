# Boyer-Moore Voting Algorithm; Time: O(n); Space: O(1)
def majority_element(nums):
    res = count = 0

    for n in nums:
        if count == 0:
            res = n

        if n == res:
            count += 1
        else:
            count -= 1

    return res


# Test cases:
print(majority_element([3, 2, 3]))
print(majority_element([2, 2, 1, 1, 1, 2, 2]))
