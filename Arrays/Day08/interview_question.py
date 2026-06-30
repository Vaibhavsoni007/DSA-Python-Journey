
"""Challenge 1

Implement Move Zeroes without using another array.


Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]"""

nums = [0,1,0,3,12]
i = 0

for j in range(0,len(nums)):
    if nums[j] != 0:
        nums[i],nums[j] = nums[j],nums[i]
        i += 1

print(nums)
    

"""Challenge 2

Merge two sorted arrays using only two pointers.

Input: arr1 = [1, 3, 5], arr2 = [2, 4, 6]
Output: [1, 2, 3, 4, 5, 6]"""

arr1 = [1,3,5]
arr2 = [2,4,6]

i,j = 0,0
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