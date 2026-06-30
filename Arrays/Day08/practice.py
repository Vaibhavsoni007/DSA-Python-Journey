"""
Problem Statement: Given an array of integers, move all 0’s to the end of it while maintaining the
relative order of the non-zero elements.

Example:
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
"""

arr = [4,0,5,0,0,3]
i = 0
# Iterate through the array with the right pointer
for j in range(0,len(arr)):
    # If the element at the right pointer is not 0
    if arr[j] != 0:
        # Swap the elements at the left and right pointers
        arr[i], arr[j] = arr[j], arr[i]
        # Increment the left pointer
        i += 1
    
print(arr)


"""
Problem Statement: Given two sorted arrays of integers, merge them into a single sorted array.

Example:
Input: arr1 = [1, 3, 5], arr2 = [2, 4, 6]
Output: [1, 2, 3, 4, 5, 6]
""" 
 
arr1 = [1,4,7]
arr2 = [2,3,6,9,11]


i , j = 0,0

result = []

while i < len(arr1) and j < len(arr2):
    if arr1[i] < arr2[j]:
        result.append(arr1[i])
        i += 1
    else:
        result.append(arr2[j])
        j += 1

while i < len(arr1):
    result.append(arr1[i])
    i += 1

while j < len(arr2):
    result.append(arr2[j])
    j += 1

print(result)       

