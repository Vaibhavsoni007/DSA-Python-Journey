# using dictionary print frequency of each number
arr = [1,2,1,3,2,1]

freq = {}
for i in range(len(arr)):
    if arr[i] in freq:
        freq[arr[i]] = freq[arr[i]] + 1
    else:
        freq[arr[i]] = 1

print(freq)
