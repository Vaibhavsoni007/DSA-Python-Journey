# arr = [1,3,5,7,9,11]

# target = 7
# arr = [10,20,30,40,50]

# target = 60
arr = [5]

target = 5
flag = 0
left = 0
right = len(arr) - 1

while left <= right:
    mid = (left + right)//2

    if arr[mid] == target:
        flag = 1
        break
    elif arr[mid] < target:
        left = mid + 1
    else:
        right = mid - 1


if flag == 1:
    print(f"target was found : {mid}")
else:
    print("target not found")

