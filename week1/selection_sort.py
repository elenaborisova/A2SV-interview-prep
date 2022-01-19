# Time: O(n^2); Space: O(1)
def selection_sort(arr, n):
    min_el_idx = 0

    for i in range(n):
        for j in range(i + 1, n):
            if arr[j] < arr[min_el_idx]:
                min_el_idx = j

        arr[i], arr[min_el_idx] = arr[min_el_idx], arr[i]
        min_el_idx = i + 1

    return arr


# Test cases:
print(selection_sort([4, 1, 3, 9, 7], 5))
