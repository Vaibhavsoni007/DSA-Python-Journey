# 📘 Container With Most Water – Interview Q&A

---

## ❓ Interview Question 1  
**Why do we move the pointer with the smaller height?**

👉 Because the area is limited by the shorter line.  
- Formula: `Area = min(height[left], height[right]) × (right - left)`  
- If we move the taller pointer, the width decreases but the limiting height stays the same → area cannot improve.  
- Moving the shorter pointer gives a chance to find a taller line, which may increase the limiting height and thus the area.

### Example
`height = [1,8,6,2,5,4,8,3,7]`

- Start: left=0 (height=1), right=8 (height=7)  
  Area = `min(1,7) × (8-0) = 8`

- Wrong move (move taller → right--):  
  New area = `min(1,3) × (7-0) = 7` (smaller)

- Correct move (move shorter → left++):  
  New area = `min(8,7) × (8-1) = 49` (much larger ✅)

---

## ❓ Interview Question 2  
**Compare both approaches.**

| Approach       | Time   | Space |
|----------------|--------|-------|
| Brute Force    | O(n²)  | O(1)  |
| Two Pointers   | O(n)   | O(1)  |

### Which one is preferred?  
- **Two Pointers** is preferred.  
- Reason: Brute force checks all pairs → too slow for large inputs.  
- Two pointers intelligently reduce the search space → linear time, very efficient.

---

## ❓ Interview Question 3  
**How is this problem different from Trapping Rain Water even though both use Two Pointers?**

- **Container With Most Water**:  
  - We only care about **two lines** at a time (left and right).  
  - The area is determined by the shorter line × distance.  
  - Two pointers move inward until they meet.

- **Trapping Rain Water**:  
  - We care about **water trapped between multiple bars**.  
  - Need to calculate water above each bar using left max and right max.  
  - Two pointers are used differently: track max heights from both sides.

### Example Difference
- Container With Most Water:  
  Input: `[1,8,6,2,5,4,8,3,7]` → Max area = 49  
- Trapping Rain Water:  
  Input: `[0,1,0,2,1,0,1,3,2,1,2,1]` → Total trapped water = 6 units

---

## ✅ Summary
- Move the **smaller pointer** because it limits the area.  
- **Two Pointers** beats brute force in efficiency.  
- Though both problems use two pointers, **Container With Most Water** focuses on max area between two lines, while **Trapping Rain Water** calculates water trapped across the whole array.

