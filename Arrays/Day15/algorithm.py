# 📖 Approach 1 - Brute Force
# ---------------------------
# For each index, multiply every other element.
# Time Complexity: O(n^2)
# Space Complexity: O(1)

def product_except_self_bruteforce(nums):
    n = len(nums)
    answer = []
    for i in range(n):
        product = 1
        for j in range(n):
            if i != j:
                product *= nums[j]
        answer.append(product)
    return answer


# 📖 Approach 2 - Division Method
# -------------------------------
# Calculate total product and divide by nums[i].
# Not valid if division is disallowed or nums contains zero.
# Time Complexity: O(n)
# Space Complexity: O(1)

def product_except_self_division(nums):
    total_product = 1
    zero_count = nums.count(0)
    
    # If more than one zero, all products will be zero
    if zero_count > 1:
        return [0] * len(nums)
    
    # Calculate product of non-zero elements
    for num in nums:
        if num != 0:
            total_product *= num
    
    answer = []
    for num in nums:
        if zero_count == 0:
            answer.append(total_product // num)
        else:
            # Only the index with zero gets non-zero product
            answer.append(total_product if num == 0 else 0)
    return answer


# 📖 Approach 3 - Prefix & Suffix Product
# ---------------------------------------
# Use prefix and suffix arrays to avoid division.
# Time Complexity: O(n)
# Space Complexity: O(n)

def product_except_self_prefix_suffix(nums):
    n = len(nums)
    
    # Step 1: Build prefix product
    prefix = [1] * n
    for i in range(1, n):
        prefix[i] = prefix[i-1] * nums[i-1]
    
    # Step 2: Build suffix product
    suffix = [1] * n
    for i in range(n-2, -1, -1):
        suffix[i] = suffix[i+1] * nums[i+1]
    
    # Step 3: Multiply prefix and suffix
    answer = [prefix[i] * suffix[i] for i in range(n)]
    return answer


# 📖 Approach 4 - Optimized Prefix & Suffix (No Extra Arrays)
# -----------------------------------------------------------
# Instead of separate prefix/suffix arrays, compute in two passes.
# Time Complexity: O(n)
# Space Complexity: O(1) (excluding output array)

def product_except_self_optimized(nums):
    n = len(nums)
    answer = [1] * n
    
    # Step 1: Prefix pass
    prefix = 1
    for i in range(n):
        answer[i] = prefix
        prefix *= nums[i]
    
    # Step 2: Suffix pass
    suffix = 1
    for i in range(n-1, -1, -1):
        answer[i] *= suffix
        suffix *= nums[i]
    
    return answer


# -------------------------------
# 🔎 Testing all approaches
nums = [1, 2, 3, 4]

print("Brute Force:", product_except_self_bruteforce(nums))
print("Division Method:", product_except_self_division(nums))
print("Prefix & Suffix:", product_except_self_prefix_suffix(nums))
print("Optimized Prefix & Suffix:", product_except_self_optimized(nums))
