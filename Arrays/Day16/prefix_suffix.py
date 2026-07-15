# 📖 Approach 2 - Prefix & Suffix Arrays
# Problem: Trapping Rain Water
# Idea:
#   - Precompute maximum height to the left of each index (leftMax[])
#   - Precompute maximum height to the right of each index (rightMax[])
#   - Water trapped at index i = min(leftMax[i], rightMax[i]) - height[i]

def trap_prefix_suffix(height):
    n = len(height)
    if n == 0:
        return 0

    # Step 1: Create arrays to store leftMax and rightMax
    leftMax = [0] * n
    rightMax = [0] * n

    # Step 2: Fill leftMax array
    leftMax[0] = height[0]
    for i in range(1, n):
        leftMax[i] = max(leftMax[i-1], height[i])

    # Step 3: Fill rightMax array
    rightMax[n-1] = height[n-1]
    for i in range(n-2, -1, -1):
        rightMax[i] = max(rightMax[i+1], height[i])

    # Step 4: Calculate trapped water
    water = 0
    for i in range(n):
        water += min(leftMax[i], rightMax[i]) - height[i]

    return water


# ✅ Example usage
if __name__ == "__main__":
    arr = [0,1,0,2,1,0,1,3,2,1,2,1]
    print("Trapped Water (Prefix & Suffix):", trap_prefix_suffix(arr))
    # Output: 6
