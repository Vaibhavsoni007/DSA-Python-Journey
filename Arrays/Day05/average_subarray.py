arr = [1,2,3,4,5]
k = 2
result = []

window_sum = sum(arr[0:k])
result.append(window_sum/k)

for i in range(k,len(arr)):
    window_sum = window_sum + arr[i] - arr[i-k]
    result.append(window_sum/k)

print(result)