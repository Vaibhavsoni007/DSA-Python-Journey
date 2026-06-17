# Day 02 - Array Operations & Two Pointers

## Goal of Day 02

Today I learned how to modify arrays.

Main operations:

- Insert
- Update
- Delete
- Introduction to Two Pointer Technique

---

# 1. Insert Operation

## Insert at End

```python
arr = [10, 20, 30]

arr.append(40)

print(arr)
```

Output:

```text
[10, 20, 30, 40]
```

Time Complexity:

```text
O(1) Average
```

---

## Insert at Specific Index

```python
arr = [10, 20, 40]

arr.insert(2, 30)

print(arr)
```

Output:

```text
[10, 20, 30, 40]
```

Time Complexity:

```text
O(n)
```

Reason:

Elements need to be shifted.

Example:

```text
Before:

[10, 20, 40]

Insert 30 at index 2

After:

[10, 20, 30, 40]
```

40 shifts one position to the right.

---

# 2. Update Operation

Changing a value at a specific index.

```python
arr = [10, 20, 30]

arr[1] = 200
```

Result:

```text
[10, 200, 30]
```

Time Complexity:

```text
O(1)
```

Reason:

Array indexing is direct.

---

# 3. Delete Operation

## Delete by Value

```python
arr = [10, 20, 30, 40]

arr.remove(30)
```

Output:

```text
[10, 20, 40]
```

Time Complexity:

```text
O(n)
```

---

## Delete by Index

```python
arr = [10, 20, 30, 40]

arr.pop(2)
```

Output:

```text
[10, 20, 40]
```

Time Complexity:

```text
O(n)
```

Reason:

Remaining elements shift left.

---

# Array Complexity Summary

| Operation | Complexity |
|------------|------------|
| Access | O(1) |
| Update | O(1) |
| Append | O(1) |
| Insert at Index | O(n) |
| Delete | O(n) |
| Traversal | O(n) |

---

# Two Pointer Technique (Important)

Today I saw my first Two Pointer problem.

The idea is:

Use two variables (pointers) for different jobs.

Example:

- Read Pointer -> Reads elements
- Write Pointer -> Stores valid elements

---

## Why Use Two Pointers?

Without Two Pointers:

- Extra loops may be required
- Complexity may become O(n²)

With Two Pointers:

- Most problems become O(n)

---

# Example

Array:

```python
nums = [1, 1, 2, 2, 3]
```

Goal:

Remove duplicates.

Process:

```text
Read Pointer -> scans array

Write Pointer -> stores unique values
```

Result:

```text
[1, 2, 3]
```

Complexity:

```text
Time: O(n)
Space: O(1)
```

---

# LeetCode 1480 - Running Sum of 1D Array

Concept Learned:

- Running Total
- Prefix Sum Foundation

My First Solution:

```text
O(n²)
```

Optimized Solution:

```text
O(n)
```

Key Learning:

Reuse previous calculations instead of recalculating everything.

---

# LeetCode 1920 - Build Array from Permutation

Formula:

```python
ans[i] = nums[nums[i]]
```

Concept Learned:

- Nested Indexing
- Array Access

Complexity:

```text
Time: O(n)
Space: O(n)
```

---

# LeetCode 26 - Remove Duplicates from Sorted Array

Concept Learned:

- Two Pointers
- In-place Modification

Important:

Do not remove elements repeatedly using pop().

Reason:

```text
pop(index) -> O(n)
```

Can make the solution O(n²).

Optimal:

```text
Time: O(n)
Space: O(1)
```

---

# LeetCode 27 - Remove Element

Concept Learned:

- Read Pointer
- Write Pointer
- In-place Modification

Idea:

Keep all valid elements at the beginning of the array.

Example:

```text
Input:

[0,1,2,2,3,0,4,2]

Remove: 2

Valid Part:

[0,1,3,0,4]
```

Complexity:

```text
Time: O(n)
Space: O(1)
```

---

# Mistakes I Made Today

1. Used variable name:

```python
sum
```

Better:

```python
running_sum
```

---

2. Used variable names:

```python
max
min
```

Better:

```python
maximum
minimum
```

Reason:

max() and min() are built-in Python functions.

---

# Key Takeaways

- Array access is O(1)
- Insert/Delete usually cost O(n)
- Update is O(1)
- Two Pointer is a very important interview pattern
- Avoid modifying arrays repeatedly inside loops
- Think about Time Complexity before writing code

---

# Questions Solved Today

## Local Practice

- Insert at End
- Insert at Index
- Update Value
- Delete by Value
- Delete by Index

## LeetCode

- 26. Remove Duplicates from Sorted Array
- 27. Remove Element

Status:

✅ Day 02 Completed