# i have to write simple beginner level code for variable window technique which will write the max sum of subarray of array

def max_sum_subarray(arr, k):
    n = len(arr)
    if n < k:
        return -1  # Not enough elements for the window size

    max_sum = 0
    window_sum = sum(arr[:k])  # Sum of the first 'k' elements
    max_sum = window_sum

    for i in range(k, n):
        window_sum += arr[i] - arr[i - k]  # Slide the window
        max_sum = max(max_sum, window_sum)

    return max_sum

# Example usage:
arr = [1, 2, 3, 4, 5]
k = 3
result = max_sum_subarray(arr, k)
print(result)