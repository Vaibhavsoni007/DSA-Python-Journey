arr = [1,2,3,4,5]
k = 3

window_sum = sum(arr[0:k])
max_sum = window_sum

for i in range(k,len(arr)):
    window_sum = window_sum + arr[i] - arr[i-k]
    max_sum = max(max_sum,window_sum)

print(max_sum)