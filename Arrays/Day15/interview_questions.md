# Product of Array Except Self – Interview Q&A

---

## ❓ Interview Question 1  
**Why is the division approach not accepted?**

- **Reason 1: Division by Zero**  
  Example: `nums = [1, 2, 0, 4]`  
  - Total product = 8  
  - At index with `0`, division is not possible.  
  - Multiple zeros make the logic even more complicated.

- **Reason 2: Interview Constraint**  
  Interviewers usually say: *“Do not use division.”*  
  This is because division makes the problem too easy and doesn’t test your algorithm skills.

---

## ❓ Interview Question 2  
**Why do prefix and suffix products work?**

- Idea: Instead of dividing, we calculate products before and after each index.  
- **Prefix product** → product of all elements before index `i`.  
- **Suffix product** → product of all elements after index `i`.  
- Multiply them together → product of all elements except `nums[i]`.

### Example  
`nums = [1, 2, 3, 4]`  

- Prefix = `[1, 1, 2, 6]`  
- Suffix = `[24, 12, 4, 1]`  
- Answer = `[1*24, 1*12, 2*4, 6*1] = [24, 12, 8, 6]`

This avoids division and works even if zeros are present.

---

## ❓ Interview Question 3  
**Compare all approaches**

| Approach            | Time   | Space | Notes |
|---------------------|--------|-------|-------|
| [Brute Force](ca://s?q=Explain_brute_force_array_product)       | O(n²) | O(1) | Simple but very slow |
| [Division](ca://s?q=Explain_division_method_array_product)       | O(n)  | O(1) | Not allowed in interviews, fails with zero |
| [Prefix + Suffix](ca://s?q=Explain_prefix_suffix_array_product) | O(n)  | O(n) | Works well, easy to understand |
| [Optimized](ca://s?q=Explain_optimized_prefix_suffix_array_product) | O(n)  | O(1)* | Best choice, efficient and accepted |

\*Ignoring the output array, as LeetCode does.

---

## ✅ Which one is preferred in interviews?

- The **Optimized Prefix + Suffix approach** is the most preferred.  
- It shows you understand:  
  - Prefix/Suffix technique  
  - Space optimization  
  - Handling edge cases (like zeros)  
- Time complexity is **O(n)** and space is **O(1)**, which is the ideal solution.

---

### 📌 Key Takeaway
- Division method is rejected.  
- Prefix + Suffix is the core idea.  
- Optimized version is the **interview-winning answer**.
