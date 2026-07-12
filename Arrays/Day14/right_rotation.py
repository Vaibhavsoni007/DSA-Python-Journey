# ---------------------------------------
# Right Rotation - Brute Force Approach
# ---------------------------------------
def right_rotate_bruteforce(arr, k):
    n = len(arr)
    k = k % n
    for _ in range(k):
        last = arr[-1]
        for i in range(n-1, 0, -1):
            arr[i] = arr[i-1]
        arr[0] = last
    return arr

# Time Complexity: O(n*k)
# Space Complexity: O(1)


# ---------------------------------------
# Right Rotation - Extra Array Approach
# ---------------------------------------
def right_rotate_extra(arr, k):
    n = len(arr)
    k = k % n
    temp = arr[-k:] + arr[:-k]
    return temp

# Time Complexity: O(n)
# Space Complexity: O(n)


# ---------------------------------------
# Right Rotation - Reversal Algorithm
# ---------------------------------------
def reverse(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

def right_rotate_reversal(arr, k):
    n = len(arr)
    k = k % n
    reverse(arr, 0, n-1)
    reverse(arr, 0, k-1)
    reverse(arr, k, n-1)
    return arr

# Time Complexity: O(n)
# Space Complexity: O(1)


# -------------------------------
# Example Usage
# -------------------------------
arr1 = [1,2,3,4,5,6,7]
print("Brute Force Right Rotation by 3:", right_rotate_bruteforce(arr1.copy(), 3))

arr2 = [1,2,3,4,5,6,7]
print("Extra Array Right Rotation by 3:", right_rotate_extra(arr2.copy(), 3))

arr3 = [1,2,3,4,5,6,7]
print("Reversal Algorithm Right Rotation by 3:", right_rotate_reversal(arr3.copy(), 3))
