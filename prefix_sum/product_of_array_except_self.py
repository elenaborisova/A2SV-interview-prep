# Time: O(n); Space: O(n)
def product_except_self(nums):
    prefix = []
    acc_prod = 1
    for n in nums:
        acc_prod *= n
        prefix.append(acc_prod)

    suffix = [0] * len(nums)
    acc_prod = 1
    for i in range(len(nums) - 1, -1, -1):
        acc_prod *= nums[i]
        suffix[i] = acc_prod

    res = []
    for i in range(len(nums)):
        prev = prefix[i - 1] if i > 0 else 1
        nextt = suffix[i + 1] if i < len(nums) - 1 else 1

        res.append(prev * nextt)

    return res


# Time: O(n); Space: O(1)
def product_except_self2(nums):
    res, prefix, suffix = [1] * len(nums), 1, 1

    for i in range(len(nums)):
        res[i] *= prefix  # prefix product from one end
        prefix *= nums[i]

        res[-1 - i] *= suffix  # suffix product from other end
        suffix *= nums[-1 - i]

    return res


# Test cases:
print(product_except_self2([1, 2, 3, 4]))
