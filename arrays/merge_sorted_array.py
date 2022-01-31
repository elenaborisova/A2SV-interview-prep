# Time: O(n + m); Space: O(1)
def merge(nums1, m, nums2, n):
    pos = m + n - 1

    while m and n:
        if nums2[n - 1] >= nums1[m - 1]:
            nums1[pos] = nums2[n - 1]
            n -= 1
        else:
            nums1[pos] = nums1[m - 1]
            m -= 1
        pos -= 1

    if n:
        for i in range(pos, -1, -1):
            nums1[i] = nums2[n - 1]
            n -= 1


# Test cases:
print(merge(nums1=[1, 2, 3, 0, 0, 0], m=3, nums2=[2, 5, 6], n=3) == [1, 2, 2, 3, 5, 6])
print(merge(nums1=[1], m=1, nums2=[], n=0) == [1])
print(merge(nums1=[2, 0], m=1, nums2=[1], n=1) == [1, 2])
print(merge(nums1=[0], m=0, nums2=[1], n=1) == [1])
print(merge(nums1=[4, 5, 6, 0, 0, 0], m=3, nums2=[1, 2, 3], n=3) == [1, 2, 3, 4, 5, 6])
print(merge(nums1=[4, 0, 0, 0, 0, 0], m=1, nums2=[1, 2, 3, 5, 6], n=5) == [1, 2, 3, 4, 5, 6])
