def kadanes_algo(arr):
    current_sum, global_sum = arr[0],arr[0]
    n = len(arr)
    
    for idx in range(1,n):
        current_sum = max(arr[idx],arr[idx] + current_sum)
        
        if current_sum > global_sum:
            global_sum = current_sum
            
    return global_sum

if __name__ == "__main__":
    arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    result = kadanes_algo(arr)
    print("sum is",result)
    
