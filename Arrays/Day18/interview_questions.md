# 📘 Spiral Traversal – Interview Q&A

---

## ❓ Interview Question 1  
**Why do we need four boundaries?**

👉 We use four boundaries (`top`, `bottom`, `left`, `right`) to control the traversal of the matrix layer by layer.  
- `top` → tracks the first row not yet traversed.  
- `bottom` → tracks the last row not yet traversed.  
- `left` → tracks the first column not yet traversed.  
- `right` → tracks the last column not yet traversed.  

This ensures we move in spiral order (left → right, top → bottom, right → left, bottom → top) without revisiting elements.

---

## ❓ Interview Question 2  
**Why are these conditions necessary?**

- `if top <= bottom`  
- `if left <= right`

👉 These conditions prevent **overlapping traversal** when the boundaries cross each other.  
- Without them, the algorithm might revisit elements or go out of bounds.  
- They act as safety checks to stop the spiral once all rows and columns are covered.

### Example
Matrix:

[1, 2]
[3, 4]

- After traversing top row and right column, `top` becomes 1 and `right` becomes 0.  
- Condition `if top <= bottom` ensures we don’t traverse the bottom row twice.

---

## ❓ Interview Question 3  
**Complexity Comparison**

| Approach          | Time       | Space |
|-------------------|------------|-------|
| Spiral Traversal  | O(m × n)   | O(1) (excluding output) |

👉 Every element is visited **exactly once** because:  
- The boundaries (`top`, `bottom`, `left`, `right`) shrink after each traversal.  
- Each loop iteration covers one full row or column.  
- No element is revisited since the boundaries move inward.  
- Thus, for a matrix of size `m × n`, total operations = `m × n`.

---

## ✅ Summary
- Four boundaries ensure controlled spiral traversal.  
- Conditions `top <= bottom` and `left <= right` prevent revisiting.  
- Time complexity is **O(m × n)** because each element is processed once.  
- Space complexity is **O(1)** (ignoring the output list).
