from maximum_subarray import kadanes_algo

# Example 1
arr = [1, 2, 3, -2, 5]
result = kadanes_algo(arr)
print("Example 1 Output:", result)  # Expected: 9

# Example 2
arr = [-5, -2, -8, -1]
result = kadanes_algo(arr)
print("Example 2 Output:", result)  # Expected: -1

# Example 3
arr = [8]
result = kadanes_algo(arr)
print("Example 3 Output:", result)  # Expected: 8

# Example 4
arr = [-2, -3, 4, -1, -2, 1, 5, -3]
result = kadanes_algo(arr)
print("Example 4 Output:", result)  # Expected: 7

# Example 5
arr = [2, 4, 6, 8]
result = kadanes_algo(arr)
print("Example 5 Output:", result)  # Expected: 20
