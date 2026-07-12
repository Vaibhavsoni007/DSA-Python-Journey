def reverse(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

def left_rotate_reversal(arr, k):
    n = len(arr)
    k = k % n
    reverse(arr, 0, k-1)
    reverse(arr, k, n-1)
    reverse(arr, 0, n-1)
    return arr

# Time Complexity: O(n)
# Space Complexity: O(1)

if __name__ == "__main__":
    # -------------------------------
    # Example Usage
    # -------------------------------
    arr1 = [1,2,3,4,5,6,7]
    print("Brute Force Left Rotation by 3:", left_rotate_bruteforce(arr1.copy(), 3))

    arr2 = [1,2,3,4,5,6,7]
    print("Extra Array Left Rotation by 3:", left_rotate_extra(arr2.copy(), 3))

    arr3 = [1,2,3,4,5,6,7]
    print("Reversal Algorithm Left Rotation by 3:", left_rotate_reversal(arr3.copy(), 3))