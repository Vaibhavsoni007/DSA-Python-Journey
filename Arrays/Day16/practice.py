from brute_force import trap_brute_force
from prefix_suffix import trap_prefix_suffix
from two_pointer import trap_two_pointer

# ✅ Example usage
height = [3,0,2,0,4]
print("Trapped Water (Brute Force):", trap_brute_force(height))  # Output: 7
print("Trapped Water (Prefix & Suffix):", trap_prefix_suffix(height))  # Output: 7
print("Trapped Water (Two Pointer Optimal):", trap_two_pointer(height))  # Output: 7

