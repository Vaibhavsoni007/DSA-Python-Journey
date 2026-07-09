def morre(arr):
    candidate = None
    count = 0
    
    # Pass 1: Find the majority candidate
    for num in arr:
        if count == 0:
            candidate = num
            count = 1
        elif candidate == num:
            count += 1
        else:
            count -= 1
            
    # Pass 2: Verify if the candidate strictly appears more than n // 2 times
    # This happens OUTSIDE the loop, running only once.
    if arr.count(candidate) > len(arr) // 2:
        return candidate
        
    return -1

if __name__ == "__main__":
    # Sample array execution
    arr = [3, 2, 3]
    result = morre(arr)
    print(f"The majority element is: {result}")  # Output: 3

    arr = [2, 3, 2, 3, 3]
    print(morre(arr))  # Output will correctly be 3
    