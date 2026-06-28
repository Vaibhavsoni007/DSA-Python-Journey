# Question 01 find the first occurrance
arr = [5]

target = 5

left = 0
right = len(arr) - 1
first = -1

while left <= right:

    mid = left + ( right - left )//2

    if arr[mid] == target:
        first = mid
        right = mid - 1

    elif arr[mid] < target:
        left = mid + 1
    
    elif arr[mid] > target:
        right = mid - 1

print(f"the first occurance of {target} is :",first)

# Question 02 find the last occurrance
arr = [1,1]

target = 2
last = -1

left = 0
right = len(arr) - 1

while left <= right:

    mid = left + ( right - left )//2

    if arr[mid] == target:
        last = mid
        left = mid + 1

    elif arr[mid] < target:
        left = mid + 1
    
    elif arr[mid] > target:
        right = mid - 1

print(f"the last occurance of {target} is :",last)