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
