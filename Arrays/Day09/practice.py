# question 1 find longest length

# longest subarray sum
def longest_subarray_sum(arr,k):
    n = len(arr)
    start = 0
    current_sum = 0
    max_length = 0
    
    for end in range(0,n):
        current_sum += arr[end]
        
        while start <= end and current_sum > k:
            current_sum -= arr[start]
            start += 1
            
        max_length = max(max_length,end-start+1)
        
    return max_length

arr = [1, 2, 3, 4, 5,6,7,8,9,10]
k = 17
result = longest_subarray_sum(arr,k)
print(f"result :{result}")

