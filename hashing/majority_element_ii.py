import collections


# Time: O(n); Space: O(n)
def majority_element(nums):
    n = len(nums)
    freq = collections.Counter(nums)
    return [el for el, fr in freq.items() if fr > n / 3]


# Boyer-Moore Voting Algorithm; Time: O(n); Space: O(1)
def majority_element2(nums):
    count1 = count2 = 0
    candidate1 = candidate2 = None

    for n in nums:
        if n == candidate1:
            count1 += 1
        elif n == candidate2:
            count2 += 1
        elif count1 == 0:
            candidate1, count1 = n, 1
        elif count2 == 0:
            candidate2, count2 = n, 1
        else:
            # Fully pairing (votes cancel each other out)
            count1 -= 1
            count2 -= 1

    return [n for n in (candidate1, candidate2)
            if nums.count(n) > len(nums) // 3]


# Test cases:
print(majority_element2([3, 2, 3]))
print(majority_element2([1]))
print(majority_element2([1, 2]))
