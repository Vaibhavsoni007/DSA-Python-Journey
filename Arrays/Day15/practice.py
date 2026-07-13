def algo(arr):
    n = len(arr)
    answer = [1] * n
    
    prefix = 1
    for index in range(n):
        answer[index] = prefix
        prefix *= arr[index]

    suffix = 1
    for index in range(n-1,-1,-1):
        answer[index] *= suffix
        suffix *= arr[index]
        
    return answer
    
arr = [1,2,3,4]
print(algo(arr))