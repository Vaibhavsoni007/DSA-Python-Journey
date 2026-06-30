"""
Problem Statement: Given an array of integers, remove the duplicates in-place
such that each element appears only once and return the new length.

Example:
Input: nums = [1,1,2,2,3]
Output: 3, nums = [1,2,3,_,_]
"""

arr = [1,1,2,2,3]
i = 0
j = 1

while j<len(arr):
    if arr[i] != arr[j]:
        i += 1
        arr[i] = arr[j]
    j = j + 1

print(arr[0:i+1])    
