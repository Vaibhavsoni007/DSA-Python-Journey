# 📘 Trapping Rain Water – Interview Notes

## ❓ Interview Question 1  
**Why does the formula use `min(leftMax, rightMax)` instead of `max(leftMax, rightMax)`?**

- Water trapped at an index depends on the **shorter boundary**.  
- Even if one side has a very tall wall, the water cannot rise above the shorter wall.  
- Example:  
height = [3, 0, 2]
leftMax = 3
rightMax = 2
min(3, 2) - height[1] = 2 - 0 = 2 units

If we used `max(3, 2)`, we’d incorrectly calculate `3 - 0 = 3`, which is impossible.

---

## ❓ Interview Question 2  
**Why is the Two Pointer approach more space efficient?**

- Prefix & Suffix arrays store extra information → **O(n) space**.  
- Two Pointer approach maintains only two variables: `leftMax` and `rightMax`.  
- No need for arrays → **O(1) space**.  
- This makes it optimal for large inputs where memory usage matters.

---

## ❓ Interview Question 3  
**Compare all approaches**

| **Approach** | **Time** | **Space** | **Notes** |
|--------------|----------|-----------|-----------|
| [Brute Force](ca://s?q=Explain_brute_force_trapping_rain_water) | O(n²) | O(1) | Simple but inefficient |
| [Prefix + Suffix](ca://s?q=Explain_prefix_suffix_trapping_rain_water) | O(n) | O(n) | Efficient but uses extra arrays |
| [Two Pointer](ca://s?q=Explain_two_pointer_trapping_rain_water) | O(n) | O(1) | Optimal, expected in interviews |

---

## ✅ Which approach is preferred in interviews? Why?

- **Two Pointer (Optimal)** is preferred.  
- Reason:  
- Same time complexity as Prefix & Suffix (O(n)).  
- But uses **constant space (O(1))**.  
- Shows understanding of optimization and problem-solving skills.  
- Interviewers often expect this solution because it balances efficiency and memory usage.

---

## 📖 Example Walkthrough (Two Pointer)

height = [0,1,0,2,1,0,1,3,2,1,2,1]

Step 1: left=0, right=11, leftMax=0, rightMax=0
Step 2: Move left → update leftMax
Step 3: Move right → update rightMax
Step 4: Calculate trapped water at each step

Final Answer = 6 units

