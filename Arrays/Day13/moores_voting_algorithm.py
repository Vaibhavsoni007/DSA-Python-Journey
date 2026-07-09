def find_majority_element(arr):
    """
    Finds the majority element in an array using Moore's Voting Algorithm.
    Assumes a majority element always exists as per the classic algorithm constraint.
    """
    candidate = None
    count = 0

    # Step 1: Find a candidate for the majority element
    for num in arr:
        # If count reaches 0, we pick the current number as the new candidate
        if count == 0:
            candidate = num
            count = 1
        # If the current number matches the candidate, increment the count
        elif num == candidate:
            count += 1
        # If it doesn't match, decrement the count
        else:
            count -= 1

    # Step 2: Optional Verification
    # (Only strictly required if a majority element might not exist in the input)
    # if arr.count(candidate) > len(arr) // 2:
    #     return candidate

    return candidate

# Sample array execution
arr = [3, 2, 3]
result = find_majority_element(arr)

print(f"The majority element is: {result}")