"""
question 1
arr = [2,1,0]
expected output = [0,1,2]

question 2
arr = [1,2,0,1,2,0]
expected output = [0,0,1,1,2,2]

question 3
arr = [0,0,0]
expected output = [0,0,0]

question 4
arr = [2,2,2]
expected output = [2,2,2]

question 5
arr = [1,1,1]
expected output = [1,1,1]
"""

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
 
   
questions = [
    [2,1,0],
    [1,2,0,1,2,0],
    [0,0,0],
    [2,2,2],
    [1,1,1]
]

for i, input_arr in enumerate(questions, start=1):
    print(f"Question {i}:")
    print(f"Input: {input_arr}")
    print(f"Expected Output: {dutch_algo(input_arr)}")
    print()