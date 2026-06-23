# Day 03 - Searching, Frequency Count & Hashing Foundation

## Goal of Day 03

Today I learned:

- Linear Search
- Frequency Count
- Duplicate Detection
- Single Number
- Introduction to Hashing
- Dictionary
- Set

---

# 1. Linear Search

Linear Search is the simplest searching algorithm.

We check every element one by one until the target is found.

Example:

```python
arr = [10,20,30,40,50]
target = 40
```

```python
for i in range(len(arr)):
    if arr[i] == target:
        print(i)
```

Output:

```text
3
```

---

## Time Complexity

Best Case:

```text
O(1)
```

Target found at first index.

Worst Case:

```text
O(n)
```

Target found at last index or not found.

---

# 2. Frequency Count

Frequency means:

How many times an element appears.

Example:

```python
arr = [1,2,1,3,2,1]
```

Output:

```text
1 -> 3
2 -> 2
3 -> 1
```

---

## Dictionary Approach

```python
freq = {}

for num in arr:

    if num in freq:
        freq[num] += 1

    else:
        freq[num] = 1
```

Result:

```python
{
    1: 3,
    2: 2,
    3: 1
}
```

---

## Time Complexity

```text
O(n)
```

---

# 3. Dictionary

Dictionary stores data in:

```text
Key : Value
```

Example:

```python
student = {
    "name": "Aman",
    "age": 21
}
```

Access:

```python
student["name"]
```

Output:

```text
Aman
```

---

## Why Dictionary Is Important?

Many O(n²) problems can be converted to:

```text
O(n)
```

using dictionaries.

---

# 4. Set

A Set stores only unique values.

Example:

```python
s = {1,2,3}
```

Duplicate values are automatically removed.

Example:

```python
s = {1,1,2,2,3}
```

Result:

```python
{1,2,3}
```

---

## Use Cases

- Remove duplicates
- Check existence quickly
- Duplicate detection

---

# 5. Contains Duplicate

Question:

Check whether an array contains duplicate values.

Example:

```python
[1,2,3,1]
```

Output:

```text
True
```

---

## Approach 1

Convert array into a set.

```python
len(nums) != len(set(nums))
```

Reason:

Set removes duplicates.

---

## Complexity

Time:

```text
O(n)
```

Space:

```text
O(n)
```

---

# 6. Single Number

Question:

Every element appears twice except one.

Find that element.

Example:

```python
[2,2,1]
```

Output:

```text
1
```

---

## Frequency Count Solution

```python
freq = {}

for num in arr:

    if num in freq:
        freq[num] += 1

    else:
        freq[num] = 1
```

Find frequency 1.

```python
for key, value in freq.items():

    if value == 1:
        print(key)
```

---

## Complexity

Time:

```text
O(n)
```

Space:

```text
O(n)
```

---

# 7. Hashing (Introduction)

Today I learned the foundation of Hashing.

Tools used:

```python
dict()
set()
```

Hashing helps in:

- Fast Searching
- Frequency Counting
- Duplicate Detection
- Optimization

---

# Complexity Comparison

| Problem | Brute Force | Optimized |
|----------|------------|------------|
| Contains Duplicate | O(n²) | O(n) |
| Frequency Count | O(n²) | O(n) |
| Single Number | O(n²) | O(n) |

---

# LeetCode Problems Solved

## 217. Contains Duplicate

Concepts:

- Set
- Hashing

Complexity:

```text
Time: O(n)
Space: O(n)
```

Status:

✅ Solved

---

## 136. Single Number

Concepts:

- Frequency Count
- Hashing

Complexity:

```text
Time: O(n)
Space: O(n)
```

Status:

✅ Solved
(If completed)

---

# Key Takeaways

- Linear Search scans elements one by one.
- Dictionary is used for frequency counting.
- Set stores unique values only.
- Hashing can reduce O(n²) problems to O(n).
- Contains Duplicate is a classic Set problem.
- Single Number can be solved using frequency counting.

---

# Questions Completed Today

## Local Practice

- Linear Search
- Frequency Count
- Duplicate Check
- Single Number

## LeetCode

- 217. Contains Duplicate
- 136. Single Number

Status:

✅ Day 03 Completed