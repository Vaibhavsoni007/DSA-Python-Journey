# Challenge 1
# Without using list.index(), find the first occurrence.
# Then demonstrate the same thing using list.index().


def first_occurrence(arr, target):
    left = 0
    right = len(arr) - 1
    first = -1

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == target:
            first = mid
            right = mid - 1
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return first


def last_occurrence(arr, target):
    left = 0
    right = len(arr) - 1
    last = -1

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == target:
            last = mid
            left = mid + 1
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return last


def count_frequency(arr, target):
    first = first_occurrence(arr, target)

    if first == -1:
        return 0

    last = last_occurrence(arr, target)
    return last - first + 1


arr = [1, 2, 2, 2, 3, 3, 4, 5]
target = 2

print("Challenge 1")
first = first_occurrence(arr, target)
print(f"First occurrence of {target} without index() is at index: {first}")

try:
    index_result = arr.index(target)
    print(f"First occurrence of {target} using index() is at index: {index_result}")
except ValueError:
    print(f"{target} is not present in the array")


# Challenge 2
# Without linear search, count frequency using first and last occurrence.

print("\nChallenge 2")
frequency = count_frequency(arr, target)
print(f"Frequency of {target} is: {frequency}")


# Challenge 3
# Binary search should work for:
# single element, duplicate elements, target not present,
# target at first index, and target at last index.

print("\nChallenge 3")

test_cases = [
    ([5], 5, "single element"),
    ([1, 2, 2, 2, 3, 4], 2, "duplicate elements"),
    ([1, 2, 3, 4, 5], 10, "target not present"),
    ([1, 2, 3, 4, 5], 1, "target at first index"),
    ([1, 2, 3, 4, 5], 5, "target at last index"),
]

for numbers, search_value, case_name in test_cases:
    first = first_occurrence(numbers, search_value)
    last = last_occurrence(numbers, search_value)
    frequency = count_frequency(numbers, search_value)

    print(f"\nCase: {case_name}")
    print(f"Array: {numbers}")
    print(f"Target: {search_value}")
    print(f"First occurrence: {first}")
    print(f"Last occurrence: {last}")
    print(f"Frequency: {frequency}")
