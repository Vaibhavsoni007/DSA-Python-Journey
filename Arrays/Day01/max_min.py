arr = [10,90,20,70,5]

max = float('-inf')

for i in range(len(arr)):
    if arr[i] > max:
        max = arr[i]

print("maximum number is ",max)

min = float('inf')

for i in range(len(arr)):
    if arr[i] < min:
        min = arr[i]

print("minimum number is ",min)