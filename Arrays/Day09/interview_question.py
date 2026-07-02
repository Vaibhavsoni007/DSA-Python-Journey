"""

Implement Variable Sliding Window without using nested loops.

Certainly! A variable sliding window technique can be implemented in Python without using nested loops. Below is an example of how to implement a variable sliding window to find the maximum sum of a subarray of size `k` in an array.```python

"""
def max_sum_subarray(arr, k):
    n = len(arr)
    if n < k:
        return -1  # Not enough elements for the window size

    max_sum = 0
    current_sum = sum(arr[:k])  # Sum of the first 'k' elements
    max_sum = current_sum

    for end in range(k, n):
        current_sum += arr[end] - arr[end - k]  # Slide the window
        max_sum = max(max_sum, current_sum)

    return max_sum
# Example usage:
arr = [1, 2, 3, 4, 5]
k = 3
result = max_sum_subarray(arr, k)
print(f"Maximum sum of subarray of size {k}: {result}")  # Output: 12 (The subarray [3, 4, 5] has the maximum sum)
