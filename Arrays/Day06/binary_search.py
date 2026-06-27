# Binary Search Implementation
# This script demonstrates how to find a target value in a sorted list
# using the binary search algorithm, which repeatedly narrows the search range.


def binary_search(numbers, target):
    left = 0
    right = len(numbers) - 1

    while left <= right:
        mid = (left + right) // 2

        if numbers[mid] == target:
            return mid

        # If the middle value is smaller, search the right half.
        if numbers[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


numbers = [2, 4, 6, 8, 10, 12, 14, 16]
target = 10

result = binary_search(numbers, target)

if result != -1:
    print(f"{target} found at index {result}")
else:
    print(f"{target} not found")


# Linear Search Implementation
# This algorithm checks each element one by one until the target is found.


def linear_search(numbers, target):
    for index in range(len(numbers)):
        if numbers[index] == target:
            return index

    return -1


linear_result = linear_search(numbers, target)

if linear_result != -1:
    print(f"{target} found at index {linear_result}")
else:
    print(f"{target} not found")
