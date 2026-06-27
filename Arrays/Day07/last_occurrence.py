def last_occurrence(arr, target):
    """
    Find the index of the last occurrence of target in a sorted array.
    
    Args:
        arr (list): Sorted list of integers
        target (int): Target value to search for
        
    Returns:
        int: Index of last occurrence, or -1 if not found
    """
    # Initialize pointers for binary search
    left, right = 0, len(arr) - 1
    result = -1

    # Perform binary search
    while left <= right:
        # Calculate mid-point (avoids integer overflow)
        mid = left + (right - left) // 2

        # If target found, store position and search right for last occurrence
        if arr[mid] == target:
            result = mid
            left = mid + 1  # Continue searching in the right half
        # If target is greater, search right half
        elif arr[mid] < target:
            left = mid + 1
        # If target is smaller, search left half
        else:
            right = mid - 1

    return result


# Test data
arr = [1, 2, 2, 2, 3, 4]
target = 2

# Display result
if __name__ == "__main__":
    result = last_occurrence(arr, target)
    print(f"Last occurrence of {target} is at index: {result}")