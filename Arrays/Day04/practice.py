# create prefix sum array 
arr = [5,10,15,20]
sum = 0
result = []
for item in arr:
    sum = sum + item
    result.append(sum)

print("the prefix sum array is ",result)


# find sum from index 1 to index 4
arr = [2,4,6,8,10]
left = int(input("Enter the starting index : "))
right = int(input("Enter the ending index : "))
sum = 0

for i in range(left,right+1):
    sum = sum + arr[i]

print(f"sum of element from index {left} to {right} is {sum}")


# prefix sum
arr = [3,3,3,3]
prefix_sum = 0

for idx in range(0,len(arr)):
    prefix_sum = prefix_sum + arr[idx]
    arr[idx] = prefix_sum

print("the prefix sum array is ",arr)