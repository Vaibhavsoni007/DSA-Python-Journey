arr = [1,1,2,5,5,6,6,3,9,3,9,8,6,6,8]

# using dictiory method
freq = {}
for i in range(0,len(arr)):
    if arr[i] in freq:
        freq[arr[i]] = freq[arr[i]] + 1
    else:
        freq[arr[i]] = 1
    
key = [k for k,v in freq.items() if v == 1]

print("the single number is",key)


# using XOR method
add = 0
for item in arr:
    add = add ^ item
print(add)