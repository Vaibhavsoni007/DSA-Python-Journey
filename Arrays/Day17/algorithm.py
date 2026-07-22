# -----------------------------------------
# 📘 Container With Most Water Problem
# -----------------------------------------

# Brute Force Approach (O(n^2))
# -----------------------------
# Idea: Check every possible pair (i, j).
# For each pair, calculate the area and keep track of the maximum.
def max_area_bruteforce(height):
    maximum = 0
    n = len(height)

    # Try all pairs
    for i in range(n):
        for j in range(i + 1, n):
            # Area = min(height[i], height[j]) * (j - i)
            area = min(height[i], height[j]) * (j - i)
            maximum = max(maximum, area)

    return maximum


# Optimal Approach - Two Pointers (O(n))
# --------------------------------------
# Idea: Use two pointers (left, right).
# Calculate area, move the pointer with the smaller height inward.
# This works because the limiting factor is the smaller height.
def max_area_two_pointers(height):
    maximum = 0
    left = 0
    right = len(height) - 1

    while left < right:
        # Calculate area
        area = min(height[left], height[right]) * (right - left)
        maximum = max(maximum, area)

        # Move the pointer with smaller height
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return maximum


# -----------------------------------------
# 🚀 Example Usage
# -----------------------------------------
if __name__ == "__main__":
    height = [1,8,6,2,5,4,8,3,7]

    print("Brute Force Result:", max_area_bruteforce(height))
    print("Two Pointers Result:", max_area_two_pointers(height))
