# Day 18 - Spiral Matrix

## Goal of Day 18

Today I learned:

- What is a Spiral Matrix?
- Four Boundary Technique
- Matrix Traversal
- Simulation Algorithm
- Dry Run
- Time & Space Complexity
- Pattern Recognition

---

# Problem Statement

Given an m × n matrix,

return all elements of the matrix in spiral order.

Example

```python
matrix = [
 [1,2,3],
 [4,5,6],
 [7,8,9]
]
```

Output

```
[1,2,3,6,9,8,7,4,5]
```

---

# What is Spiral Traversal?

Instead of traversing row by row,

we move around the matrix layer by layer.

Direction

```
→ → →

      ↓

← ← ←

↑
```

After completing one layer,

we move towards the inner layer.

---

# Four Boundaries

To traverse the matrix,

maintain four boundaries.

```
top = 0

bottom = rows - 1

left = 0

right = columns - 1
```

These boundaries shrink after every traversal.

---

# Traversal Order

Always move in this order.

Step 1

```
Left → Right
```

Traverse the Top Row.

After finishing,

```
top += 1
```

---

Step 2

```
Top → Bottom
```

Traverse the Right Column.

After finishing,

```
right -= 1
```

---

Step 3

```
Right → Left
```

Traverse the Bottom Row.

Only if

```
top <= bottom
```

After finishing,

```
bottom -= 1
```

---

Step 4

```
Bottom → Top
```

Traverse the Left Column.

Only if

```
left <= right
```

After finishing,

```
left += 1
```

Repeat until

```
top > bottom

OR

left > right
```

---

# Dry Run

Matrix

```
1 2 3

4 5 6

7 8 9
```

Initial

```
top = 0
bottom = 2

left = 0
right = 2
```

Top Row

```
1 2 3
```

Right Column

```
6 9
```

Bottom Row

```
8 7
```

Left Column

```
4
```

Remaining Matrix

```
5
```

Final Output

```
1 2 3 6 9 8 7 4 5
```

---

# Why do we need boundary checks?

Before traversing

Bottom Row

we check

```
top <= bottom
```

Before traversing

Left Column

we check

```
left <= right
```

These conditions prevent visiting the same element twice,

especially in

- Single Row Matrix
- Single Column Matrix
- Odd Sized Matrix

---

# Example

Single Row

```
1 2 3 4
```

Without the boundary check,

elements would be printed twice.

---

# Complexity

Rows = m

Columns = n

Every element is visited exactly once.

Time Complexity

```
O(m × n)
```

Space Complexity

```
O(1)
```

(Output array is not counted as extra space.)

---

# Advantages

- Every element is visited exactly once.
- No extra matrix required.
- Works for rectangular and square matrices.
- Frequently asked interview problem.

---

# Common Mistakes

- Forgetting to update top.
- Forgetting to update bottom.
- Forgetting to update left.
- Forgetting to update right.
- Missing boundary checks.
- Traversing the same row or column twice.

---

# Interview Tips

Whenever you hear

- Spiral Matrix
- Matrix Traversal
- Clockwise Traversal
- Layer by Layer

Immediately think

**Four Boundary Technique**

---

# Pattern Recognition

This approach is useful when

- Matrix traversal is required.
- Boundaries shrink after every iteration.
- Clockwise or anti-clockwise movement is involved.

---

# LeetCode Problems

## 54. Spiral Matrix

Difficulty

Medium

Pattern

Simulation

Four Boundary Technique

Status

✅ Solved

---

## Bonus Reading

59. Spiral Matrix II

Difficulty

Medium

Status

📖 Problem Read

---

# Questions Completed Today

## Local Practice

- Spiral Traversal
- Boundary Updates
- Dry Runs
- Practice Questions
- Interview Questions

## LeetCode

- 54. Spiral Matrix

---

# Key Takeaways

- Four boundaries control traversal.
- Traversal order:

```
Top

↓

Right

↓

Bottom

↓

Left
```

- Shrink the boundaries after every step.
- Boundary checks prevent duplicate traversal.
- Every element is visited exactly once.

---

# Status

✅ Day 18 Completed