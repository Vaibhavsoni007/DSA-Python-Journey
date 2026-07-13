# Day 15 - Product of Array Except Self

## Goal of Day 15

Today I learned:

- What is Product of Array Except Self?
- Brute Force Approach
- Division Approach
- Why Division is Not Preferred
- Prefix Product
- Suffix Product
- Optimal Solution
- Handling Arrays Containing Zero
- Time & Space Complexity

---

# Problem Statement

Given an integer array `nums`, return an array `answer` such that

answer[i] = product of all elements except nums[i].

Example

```python
nums = [1,2,3,4]
```

Output

```text
[24,12,8,6]
```

Explanation

Index 0

```
2 × 3 × 4 = 24
```

Index 1

```
1 × 3 × 4 = 12
```

Index 2

```
1 × 2 × 4 = 8
```

Index 3

```
1 × 2 × 3 = 6
```

---

# Brute Force Approach

For every index,

multiply every other element except itself.

Pseudo Code

```
for every i
    product = 1

    for every j
        if i != j
            product *= nums[j]

    answer.append(product)
```

## Complexity

Time

```
O(n²)
```

Space

```
O(1)
```

Works correctly,

but is too slow for large inputs.

---

# Division Approach

Calculate

```python
total_product = product of all elements
```

Then

```python
answer[i] = total_product // nums[i]
```

Example

```python
nums = [1,2,3,4]
```

Total Product

```
24
```

Answer

```
24/1 = 24

24/2 = 12

24/3 = 8

24/4 = 6
```

---

# Why is Division Not Preferred?

## Problem 1

Division by Zero

```python
nums = [1,2,0,4]
```

Total Product

```
0
```

Now

```
0 / 0
```

is invalid.

---

## Problem 2

Interviewers usually mention

```
Do NOT use division.
```

Therefore,

this approach is rejected in coding interviews.

---

# Prefix Product

Prefix Product stores the multiplication of all elements before the current index.

Example

```python
nums = [1,2,3,4]
```

Prefix

```
[1,1,2,6]
```

Explanation

| Index | Prefix |
|------|--------|
|0|1|
|1|1|
|2|2|
|3|6|

Meaning

```
prefix[i]

=

product of elements before index i
```

---

# Suffix Product

Suffix Product stores the multiplication of all elements after the current index.

Example

```python
nums = [1,2,3,4]
```

Suffix

```
[24,12,4,1]
```

Meaning

| Index | Suffix |
|------|--------|
|0|24|
|1|12|
|2|4|
|3|1|

```
suffix[i]

=

product of elements after index i
```

---

# Optimal Solution

For every index

```
answer[i]

=

prefix[i]

×

suffix[i]
```

Example

Prefix

```
[1,1,2,6]
```

Suffix

```
[24,12,4,1]
```

Multiply

```
1 × 24 = 24

1 × 12 = 12

2 × 4 = 8

6 × 1 = 6
```

Final Answer

```
[24,12,8,6]
```

---

# Dry Run

Input

```python
nums = [3,1,2,5]
```

| Index | Prefix | Suffix | Answer |
|------|--------|--------|--------|
|0|1|10|10|
|1|3|10|30|
|2|3|5|15|
|3|6|1|6|

Final Answer

```
[10,30,15,6]
```

---

# Handling Zeroes

Example

```python
nums = [1,2,0,4]
```

Output

```
[0,0,8,0]
```

Reason

Only the index containing zero receives the product of all non-zero elements.

Every other position includes multiplication by zero.

---

# Space Optimization

Instead of creating two extra arrays,

we can

- store prefix products directly inside the answer array
- keep only one variable for suffix product

This reduces extra space to

```
O(1)
```

(ignoring the output array)

This is the solution expected in interviews and on LeetCode.

---

# Complexity Comparison

| Approach | Time | Space |
|----------|------|--------|
| Brute Force | O(n²) | O(1) |
| Division | O(n) | O(1) |
| Prefix + Suffix Arrays | O(n) | O(n) |
| Optimized | O(n) | O(1)* |

*Output array is not counted as extra space.

---

# Advantages

- No division required.
- Handles zero correctly.
- Linear time complexity.
- Interview-friendly solution.
- Space optimization possible.

---

# Common Mistakes

- Using division when prohibited.
- Initializing prefix/suffix arrays incorrectly.
- Forgetting to initialize prefix and suffix with 1.
- Not handling arrays containing zero.
- Returning prefix or suffix instead of the final answer.

---

# Interview Tips

Whenever you hear

- Product Except Self
- Prefix Product
- Suffix Product
- No Division

Immediately think

**Prefix Product + Suffix Product**

---

# Pattern Recognition

Use this approach when

- Product of elements before current index is needed.
- Product of elements after current index is needed.
- Division is not allowed.
- O(n) solution is expected.

---

# LeetCode Problems

## 238. Product of Array Except Self

Difficulty

Medium

Pattern

Prefix Product

Suffix Product

Status

✅ Solved

---

## Bonus Reading

42. Trapping Rain Water

Difficulty

Hard

Status

📖 Problem Read

---

# Questions Completed Today

## Local Practice

- Prefix Product
- Suffix Product
- Product Except Self
- Practice Questions
- Interview Questions

## LeetCode

- 238. Product of Array Except Self

---

# Key Takeaways

- Division approach is not accepted in interviews.
- Prefix Product stores multiplication before an index.
- Suffix Product stores multiplication after an index.
- Final Answer = Prefix × Suffix.
- Space can be optimized to O(1).
- This is one of the most frequently asked interview questions.

---

# Status

✅ Day 15 Completed