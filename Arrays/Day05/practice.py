# find maximum sum
arr = [2,1,5,1,3,2]
k = 3

window_sum = sum(arr[0:k])
max_sum = window_sum

for i in range(k,len(arr)):
    window_sum = window_sum + arr[i] - arr[i-k]
    max_sum = max(max_sum,window_sum)

print(max_sum)

# find average
arr = [5,5,5,5]
k = 2
result = []

window_sum = sum(arr[0:k])
result.append(window_sum/k)

for i in range(k,len(arr)):
    window_sum = window_sum + arr[i] - arr[i-k]
    result.append(window_sum/k)

print(result)

# find maximum sum ( again )
arr = [10,20,30,40]
k = 2

window_sum = sum(arr[0:k])
max_sum = window_sum

for i in range(k,len(arr)):
    window_sum = window_sum + arr[i] - arr[i-k]
    max_sum = max(max_sum,window_sum)

print(max_sum)