# Time: O(n); Space: O(1)
def max_turbulence_size(arr):
    max_size = 1
    l = r = 0

    while r < len(arr):

        while l < len(arr) - 1 and arr[l] == arr[l + 1]:
            l += 1

        while r < len(arr) - 1 and (arr[r - 1] > arr[r] < arr[r + 1] or arr[r - 1] < arr[r] > arr[r + 1]):
            r += 1

        max_size = max(max_size, r - l + 1)
        l = r
        r += 1

    return max_size


# Test cases:
print(max_turbulence_size([9, 4, 2, 10, 7, 8, 8, 1, 9]))
print(max_turbulence_size([4, 8, 12, 16]))
print(max_turbulence_size([100, 100, 100]))
print(max_turbulence_size([0, 1, 1, 0, 1, 0, 1, 1, 0, 0]))
print(max_turbulence_size([1, 1, 1, 1, 1, 1, 1, 1, 1, 2]))
print(max_turbulence_size([1, 1, 2]))
