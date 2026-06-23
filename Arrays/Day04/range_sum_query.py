# range sum query 
arr = [1,2,3,4,5]
left = int(input("enter the left index of array : "))
right = int(input("enter the right index of array : "))

sum = 0
for i in range(left,right+1):
    sum = sum + arr[i]
print("the sum is ",sum)