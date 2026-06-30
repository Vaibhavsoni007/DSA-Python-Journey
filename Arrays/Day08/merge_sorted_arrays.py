"""
Problem Statement: Given two sorted arrays of integers, merge them into a single sorted array.

Example:
Input: arr1 = [1, 3, 5], arr2 = [2, 4, 6]
Output: [1, 2, 3, 4, 5, 6]
"""

# Initialize two pointers for both arrays
arr1 = [1, 3, 5, 6, 7]
arr2 = [2, 4, 6, 8, 9, 10]

i, j = 0, 0
result = []

# Merge the two arrays
while i < len(arr1) and j < len(arr2):
    if arr1[i] < arr2[j]:
        result.append(arr1[i])
        i += 1
    else:
        result.append(arr2[j])
        j += 1

# Add remaining elements of arr1
while i < len(arr1):
    result.append(arr1[i])
    i += 1

# Add remaining elements of arr2
while j < len(arr2):
    result.append(arr2[j])
    j += 1

print(result)   


"""
Time Complexity: O(n + m)
Space Complexity: O(n + m)
"""