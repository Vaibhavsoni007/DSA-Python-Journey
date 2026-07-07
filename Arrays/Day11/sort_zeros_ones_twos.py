# re-writing the code of dutch algorithm for practice :

def dutch_algo(arr):
    low = 0
    mid = 0
    high = len(arr)-1
    
    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        elif arr[mid] == 2:
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1
            
    return arr
    
arr = [2,1,2,1,0,2,0,0,1]
result = dutch_algo(arr)
print("result of dutch algo is : ",result)
