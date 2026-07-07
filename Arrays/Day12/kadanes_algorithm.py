"""
================================================================================
                           KADANE'S ALGORITHM
================================================================================
Problem Statement:
Given an integer array, find the contiguous subarray (containing at least one 
number) which has the largest sum and return its sum.

How It Works (The Core Intuition):
--------------------------------------------------------------------------------
Kadane's Algorithm looks at the array as a sequence of choices. As we iterate 
through the array, we look at each element and ask a simple question:
    
    "Is it better to add this element to our existing subarray, 
     or should we start a brand-new subarray right here?"

If the accumulated sum (`max_current`) becomes negative, adding it to the next 
element will only drag that element's value down. In that case, we "reset" and 
start our subarray fresh from the current element.

Key Variables:
--------------
1. `max_current` : Tracks the maximum subarray sum ending at the current position.
2. `max_global`  : Tracks the absolute maximum subarray sum found so far across 
                   the entire array.

Complexity:
-----------
- Time Complexity: O(n) -> We only loop through the array exactly once.
- Space Complexity: O(1) -> We only use a couple of variables for tracking.
================================================================================
"""

def kadanes_algorithm(arr):
    # Edge case: If the array is empty, return 0
    if not arr:
        return 0
    
    # Initialize both tracking variables with the first element of the array
    max_current = arr[0]
    max_global = arr[0]
    
    # Iterate through the array starting from the second element (index 1)
    for i in range(1, len(arr)):
        # Decision: Either extend the existing subarray OR start a new one here
        max_current = max(arr[i], max_current + arr[i])
        
        # If the current subarray sum is the best we've seen so far, update global
        if max_current > max_global:
            max_global = max_current
            
    return max_global


# ================================================================================
#                               EXAMPLE EXECUTION
# ================================================================================
if __name__ == "__main__":
    # Test array from the prompt
    arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    
    print("--- Kadane's Algorithm Execution ---")
    print(f"Input Array: {arr}")
    
    # Run the algorithm
    result = kadanes_algorithm(arr)
    
    # Expected Output: 6 (The subarray is [4, -1, 2, 1])
    print(f"Maximum sum of a contiguous subarray: {result}")
    print("-" * 36)