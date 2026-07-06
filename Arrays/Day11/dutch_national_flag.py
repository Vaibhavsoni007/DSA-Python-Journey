# can you write the code to demonstrate dutch national flag problem in python?
# 
# Sure! The Dutch National Flag problem is a classic algorithmic problem that involves sorting an array of three distinct elements. The goal is to rearrange the elements in such a way that all instances of the first element come first, followed by all instances of the second element, and finally all instances of the third element. Here's a Python implementation of the Dutch National Flag problem:

# input array arr = [2,0,2,1,1,0]
# output should be [0,0,1,1,2,2]

def dutch_national_flag(arr):
    low = 0
    mid = 0
    high = len(arr) - 1

    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:  # arr[mid] == 2
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1

    return arr

# Example usage:
arr = [2, 0, 2, 1, 1, 0]
sorted_arr = dutch_national_flag(arr)
print(sorted_arr)  # Output: [0, 0, 1, 1, 2, 2]
