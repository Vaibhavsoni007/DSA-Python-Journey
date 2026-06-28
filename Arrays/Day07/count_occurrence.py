# ------------------- first occurance of the number -------------------
arr = [1,2,2,2,3,3,3,3,4]
target = 3

left = 0
right = len(arr) - 1
first = -1
last = -1

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

# ------------------- last occurance of the number -------------------

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

# ------------------- count occurance of the number -------------------

if first == -1:
    count = 0
else:
    count = last - first + 1

print(f"total count of the {target} in array is : ",count)
