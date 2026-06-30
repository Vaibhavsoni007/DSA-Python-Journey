"""
Problem Statement: Given an array nums, move all 0’s to the end of it while maintaining the
relative order of the non-zero elements.

Example:
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
"""

arr = [0,1,0,3,12]

# Initialize the left pointer
i = 0

# Iterate through the array with the right pointer
for j in range(0,len(arr)):
    # If the element at the right pointer is not 0
    if arr[j] != 0:
        # Swap the elements at the left and right pointers
        arr[j],arr[i] = arr[i],arr[j]
        
        # Increment the left pointer
        i += 1  

print(arr)
    