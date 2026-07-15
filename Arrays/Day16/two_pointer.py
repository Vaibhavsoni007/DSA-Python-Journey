# 📖 Approach 3 - Two Pointer (Optimal)
# Problem: Trapping Rain Water
# Idea:
#   - Use two pointers (left, right) starting from both ends.
#   - Maintain leftMax and rightMax while traversing.
#   - Move the pointer with the smaller height because
#     trapped water depends on the smaller boundary.
#   - This avoids extra arrays → O(1) space.

def trap_two_pointer(height):
    n = len(height)
    if n == 0:
        return 0

    # Initialize pointers
    left, right = 0, n - 1
    leftMax, rightMax = 0, 0
    water = 0

    # Traverse until pointers meet
    while left <= right:
        if height[left] <= height[right]:
            # Case 1: Left side is smaller
            if height[left] >= leftMax:
                leftMax = height[left]   # update leftMax
            else:
                water += leftMax - height[left]  # trapped water
            left += 1
        else:
            # Case 2: Right side is smaller
            if height[right] >= rightMax:
                rightMax = height[right]  # update rightMax
            else:
                water += rightMax - height[right]  # trapped water
            right -= 1

    return water


# ✅ Example usage
if __name__ == "__main__":
    arr = [0,1,0,2,1,0,1,3,2,1,2,1]
    print("Trapped Water (Two Pointer Optimal):", trap_two_pointer(arr))
    # Output: 6
