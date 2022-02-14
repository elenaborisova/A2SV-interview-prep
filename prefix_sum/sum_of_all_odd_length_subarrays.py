# Time: O(n^2); Space: O(1)
def sum_odd_length_subarrays(arr):
    cum_sum = arr[0]
    for i in range(1, len(arr)):
        cum_sum += arr[i]
        arr[i] += arr[i - 1]

    for i in range(0, len(arr)):
        for j in range(i + 2, len(arr), 2):
            prev_sum = arr[i - 1] if i > 0 else 0
            cum_sum += arr[j] - prev_sum

    return cum_sum


# Test cases:
print(sum_odd_length_subarrays([1, 4, 2, 5, 3]))
print(sum_odd_length_subarrays([1, 2]))
print(sum_odd_length_subarrays([10, 11, 12]))
