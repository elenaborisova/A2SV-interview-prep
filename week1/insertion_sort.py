# Time: O(n^2); Space: O(1)
def insertion_sort1(n, arr):
    temp = arr[n - 1]

    for i in range(n - 1, -1, -1):
        if temp < arr[i - 1]:
            if i == 0:
                arr[i] = temp
                print(' '.join(map(str, arr)))
                break

            arr[i] = arr[i - 1]
            print(' '.join(map(str, arr)))
        else:
            arr[i] = temp
            print(' '.join(map(str, arr)))
            break


# Time: O(n^2); Space: O(1)
def insertion_sort2(n, arr):
    for i in range(1, n):
        temp = arr[i]

        j = i - 1
        while j >= 0 and temp < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = temp

    return arr


# Test cases:
print(insertion_sort1(5, [1, 2, 4, 5, 3]))
print(insertion_sort1(5, [2, 4, 6, 8, 3]))
print(insertion_sort1(2, [2, 1]))

print(insertion_sort2(5, [5, 4, 3, 2, 1]))
