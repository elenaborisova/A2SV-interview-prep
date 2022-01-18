# Time: O(n log n); Space: O(n)
def smaller_numbers_than_current(nums):
    d = {}
    for i, n in enumerate(sorted(nums)):
        if n not in d:
            d[n] = i

    res = []
    for n in nums:
        res.append(d[n])

    return res


# Bucket Sort; Time: O(n); Space: O(n)
def smaller_numbers_than_current2(nums):
    buckets = [0] * (max(nums) + 1)

    for num in nums:
        buckets[num] += 1

    numbers_sum = 0
    for i, bucket in enumerate(buckets):
        if bucket != 0:
            buckets[i] = numbers_sum
            numbers_sum += bucket

    return [buckets[num] for num in nums]


# Test cases:
print(smaller_numbers_than_current2([8, 1, 2, 2, 3]))
print(smaller_numbers_than_current2([6, 5, 4, 8]))
print(smaller_numbers_than_current2([7, 7, 7, 7]))
print(smaller_numbers_than_current2([7]))
