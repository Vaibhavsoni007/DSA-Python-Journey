# Day 08 - Advanced Two Pointers

## Goal of Day 08

Today I learned:

- Advanced Two Pointer Pattern
- Move Zeroes
- Merge Two Sorted Arrays
- Remove Duplicates Revision
- In-place Array Modification
- Interview Problems using Two Pointers

---

# 1. What are Two Pointers?

Two Pointer is a technique where two indices are used to solve problems efficiently.

Instead of using nested loops, we move one or both pointers based on the problem.

Benefits:

- Reduces Time Complexity
- Uses Constant Extra Space
- Very common in Interviews

---

# Types of Two Pointer Problems

## 1. Same Direction

Example:

```text
i → →
j → →
```

Used in:

- Remove Duplicates
- Remove Element
- Move Zeroes

---

## 2. Opposite Direction

Example:

```text
Left →      ← Right
```

Used in:

- Two Sum II
- Container With Most Water
- Trapping Rain Water
- Palindrome Checking

---

# 2. Move Zeroes

Problem:

Move all zeroes to the end while maintaining the order of non-zero elements.

Example:

```python
arr = [0,1,0,3,12]
```

Output:

```python
[1,3,12,0,0]
```

---

## Logic

Maintain a pointer `j` for the position where the next non-zero element should be placed.

Traverse the array:

- If the current element is non-zero:
  - Swap it with `arr[j]`
  - Increment `j`

---

## Complexity

Time:

```text
O(n)
```

Space:

```text
O(1)
```

---

# 3. Merge Two Sorted Arrays

Problem:

Merge two sorted arrays into one sorted array.

Example:

```python
arr1 = [1,3,5]
arr2 = [2,4,6]
```

Output:

```python
[1,2,3,4,5,6]
```

---

## Two Pointer Logic

Maintain:

```text
i → arr1

j → arr2
```

Compare both values.

Smaller value goes into the result.

Move only that pointer.

Repeat until one array finishes.

Then copy the remaining elements.

---

## Interview Optimization

LeetCode 88 asks for an **in-place merge**.

Instead of creating another array,

start filling `nums1` from the end.

This gives:

```text
Space = O(1)
```

---

# 4. Remove Duplicates (Revision)

Already solved earlier.

Important idea:

Maintain two pointers.

One pointer keeps track of the next unique position.

The second pointer scans the array.

---

# Pattern Recognition

Whenever you see:

- Sorted Array
- Two Arrays
- In-place Modification
- Remove Duplicates
- Move Elements
- Merge Arrays

Think about:

```text
Two Pointer
```

---

# Complexity Comparison

| Problem | Time | Space |
|---------|------|--------|
| Move Zeroes | O(n) | O(1) |
| Remove Duplicates | O(n) | O(1) |
| Merge Two Arrays (Extra Array) | O(m+n) | O(m+n) |
| Merge Two Arrays (In-place) | O(m+n) | O(1) |

---

# LeetCode Problems

## 283. Move Zeroes

Pattern:

Two Pointer

Difficulty:

Easy

Status:

✅ Solved

---

## 88. Merge Sorted Array

Pattern:

Two Pointer

Difficulty:

Easy

Status:

✅ Solved

---

## 977. Squares of a Sorted Array

Pattern:

Two Pointer

Difficulty:

Easy

Status:

✅ Solved

---

# Common Mistakes

- Forgetting to move the correct pointer.
- Accessing an index after incrementing it.
- Forgetting to copy remaining elements after one array ends.
- Returning a new array when the question asks for in-place modification.

---

# Interview Tips

Whenever an array problem mentions:

- Sorted Array
- In-place
- Constant Space
- Merge
- Remove
- Shift Elements

Always check if a Two Pointer solution exists before using nested loops.

---

# Key Takeaways

- Two Pointer reduces unnecessary comparisons.
- Move Zeroes is a classic in-place problem.
- Merge Sorted Array teaches pointer synchronization.
- In-place modification is a frequently tested interview skill.
- Recognizing patterns is more important than memorizing code.

---

# Questions Completed Today

## Local Practice

- Move Zeroes
- Merge Sorted Arrays
- Remove Duplicates Revision
- Two Pointer Practice Questions
- Interview Questions

## LeetCode

- 283. Move Zeroes
- 88. Merge Sorted Array
- 977. Squares of a Sorted Array

Status:

✅ Day 08 Completed