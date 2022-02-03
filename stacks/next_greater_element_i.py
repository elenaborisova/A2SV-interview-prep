# Time: O(n); Space: O(n)
def next_greater_element(nums1, nums2):
    stack = []
    d = {}

    i = len(nums2) - 1
    while i >= 0:
        num = nums2[i]

        if not stack:
            d[num] = -1
            stack.append(num)
            i -= 1
        elif stack[-1] > num:
            d[num] = stack[-1]
            stack.append(num)
            i -= 1
        else:
            stack.pop()

    ans = []
    for num in nums1:
        ans.append(d[num])

    return ans


# Better implementation
def next_greater_element2(nums1, nums2):
    d = {}
    stack = []

    for i in range(len(nums2) - 1, -1, -1):
        num = nums2[i]

        while stack and stack[-1] <= num:
            stack.pop()
        if stack:
            d[num] = stack[-1]
        else:
            d[num] = -1
        stack.append(num)

    return [d[num] for num in nums1]


# Test cases:
print(next_greater_element(nums1=[4, 1, 2], nums2=[1, 3, 4, 2]))
print(next_greater_element(nums1=[2, 4], nums2=[1, 2, 3, 4]))
