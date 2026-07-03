# ------------------  Bubble sort  ------------------

def Bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    
    return arr
        
# implementaion of bubble sort        
arr = [9,4,7,1,5]
result = Bubble_sort(arr)
print("Bubble sort :: ",result)
# [1,4,5,7,9] expected result

# ------------------  selection sort  ------------------

def Selection_sort(arr):
    n = len(arr)
    for i in range(0,n):
        min_idx = i
        for j in range(i+1,n):
            if arr[j] < arr[min_idx]:
                min_idx = j
            
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        
    return arr
    
# implementaion of bubble sort        
arr1 = [9,4,7,1,5]
result1 = Selection_sort(arr1)
print("Selection sort :: ",result1)
# [1,4,5,7,9] expected result

# ------------------  insertion sort  ------------------

def insertion_sort(arr):
    n = len(arr)
    
    for i in range(n):
        key = arr[i]
        j = i - 1
        
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
        
    return arr

# implementaion of insertion sort        
arr2 = [9,4,7,1,5]
result2 = insertion_sort(arr2)
print("insertion sort :: ",result2)
# [1,4,5,7,9] expected result