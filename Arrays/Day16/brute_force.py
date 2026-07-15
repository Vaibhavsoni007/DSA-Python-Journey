# 📖 Approach 1 - Brute Force
# Problem: Trapping Rain Water
# For each index, find:
#   - Maximum element on the left
#   - Maximum element on the right
# Then calculate trapped water as:
#   min(leftMax, rightMax) - height[i]

def trap_brute_force(height):
    # Initialize result
    water = 0
    n = len(height)

    # Loop through each element
    for i in range(n):
        # Step 1: Find maximum height on the left side of index i
        leftMax = max(height[:i+1])   # includes current element

        # Step 2: Find maximum height on the right side of index i
        rightMax = max(height[i:])    # includes current element

        # Step 3: Water trapped at index i
        water += min(leftMax, rightMax) - height[i]

    return water


# ✅ Example usage
if __name__ == "__main__":
    arr = [0,1,0,2,1,0,1,3,2,1,2,1]
    print("Trapped Water (Brute Force):", trap_brute_force(arr))
    # Output: 6
