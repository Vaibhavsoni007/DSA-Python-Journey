# Day 01 - Array Basics

## What is an Array?

An array is a collection of elements stored in contiguous memory locations.

In Python, we generally use Lists to represent arrays.

Example:

```python
arr = [10, 20, 30, 40, 50]
```

---

## Indexing

Every element has an index.

```python
arr[0] = 10
arr[1] = 20
arr[2] = 30
```

Last element:

```python
arr[-1]
```

---

## Traversal

Traversing means visiting every element exactly once.

Example:

```python
for i in range(len(arr)):
    print(arr[i])
```

Time Complexity:

```text
O(n)
```

---

## Reverse Traversal

Example:

```python
for i in range(len(arr)-1, -1, -1):
    print(arr[i])
```

Time Complexity:

```text
O(n)
```

---

## Finding Maximum Element

Logic:

1. Assume first element is maximum.
2. Compare with every other element.
3. Update maximum whenever a larger element is found.

Example:

```python
maximum = arr[0]

for i in range(1, len(arr)):
    if arr[i] > maximum:
        maximum = arr[i]
```

Time Complexity:

```text
O(n)
```

---

## Finding Minimum Element

Logic:

1. Assume first element is minimum.
2. Compare with every other element.
3. Update minimum whenever a smaller element is found.

Example:

```python
minimum = arr[0]

for i in range(1, len(arr)):
    if arr[i] < minimum:
        minimum = arr[i]
```

Time Complexity:

```text
O(n)
```

---

## Time Complexity Summary

| Operation | Complexity |
|------------|------------|
| Access | O(1) |
| Traversal | O(n) |
| Find Maximum | O(n) |
| Find Minimum | O(n) |

---

## LeetCode Problems Solved

### 1480. Running Sum of 1D Array

Concept:
- Prefix Sum Foundation
- Running Total

Complexity:

```text
Time: O(n)
Space: O(1) to O(n)
```

---

### 1920. Build Array from Permutation

Concept:
- Array Indexing
- Nested Index Access

Formula:

```python
ans[i] = nums[nums[i]]
```

Complexity:

```text
Time: O(n)
Space: O(n)
```

---

## Key Learnings

- Arrays store multiple values.
- Indexing starts from 0.
- Traversal visits every element.
- Maximum and Minimum can be found in one pass.
- Running Sum introduces Prefix Sum thinking.
- Nested indexing is common in interview questions.