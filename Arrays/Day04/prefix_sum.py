# prefix sum 
arr = [1,2,3,4,5]
sum = 0
result = []
for item in arr:
    sum = item + sum
    result.append(sum)

print(result)