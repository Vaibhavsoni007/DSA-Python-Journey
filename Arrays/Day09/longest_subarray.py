# longest subarray sum with sum <= k
def longest_subarray_sum(arr, k):
    n = len(arr)
    max_length = 0
    current_sum = 0
    start = 0

    for end in range(n):
        current_sum += arr[end]

        while current_sum > k and start <= end:
            current_sum -= arr[start]
            start += 1

        max_length = max(max_length, end - start + 1)

    return max_length

# Example usage:
arr = [1, 2, 3, 4, 5]
k = 7
result = longest_subarray_sum(arr, k)
print(f"Result: {result}")  # Output: 3 (The longest subarray is [1, 2, 3] with sum 6 which is <= 7)
