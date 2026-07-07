# Day 12 - Kadane's Algorithm (Maximum Subarray)

## Goal of Day 12

Today I learned:

- What is a Contiguous Subarray?
- Brute Force Approach
- Kadane's Algorithm
- Why Kadane's Algorithm works
- Handling All Negative Numbers
- Maximum Subarray Problem
- Time & Space Complexity

---

# What is a Contiguous Subarray?

A contiguous subarray contains consecutive elements from the original array.

Example

```python
arr = [2, -1, 3, 4]
```

Valid Subarrays

```text
[2]
[-1]
[3]
[4]
[2,-1]
[-1,3]
[3,4]
[2,-1,3]
[-1,3,4]
[2,-1,3,4]
```

Invalid

```text
[2,3]
```

Because `-1` is skipped.

---

# Problem Statement

Find the maximum possible sum of a contiguous subarray.

Example

```python
arr = [-2,1,-3,4,-1,2,1,-5,4]
```

Output

```text
6
```

Maximum Sum Subarray

```text
[4,-1,2,1]
```

---

# Brute Force Approach

Generate every possible subarray.

Calculate the sum of each subarray.

Return the largest sum.

---

## Complexity

Time

```text
O(n²)
```

Space

```text
O(1)
```

Works correctly but becomes slow for large arrays.

---

# Kadane's Algorithm

## Main Idea

Maintain two variables:

```python
current_sum
maximum_sum
```

Traverse the array only once.

For every element:

```python
current_sum += arr[i]
maximum_sum = max(maximum_sum, current_sum)
```

If

```python
current_sum < 0
```

Reset

```python
current_sum = 0
```

---

# Why Does It Work?

A negative running sum can never increase the sum of a future subarray.

Instead of carrying a negative sum forward,

it is better to start a new subarray.

---

# Dry Run

Input

```python
arr = [-2,1,-3,4,-1,2,1,-5,4]
```

| Index | Value | Current Sum | Maximum Sum |
|------|------|-------------|-------------|
|0|-2|-2|-2|
|Reset||0|-2|
|1|1|1|1|
|2|-3|-2|1|
|Reset||0|1|
|3|4|4|4|
|4|-1|3|4|
|5|2|5|5|
|6|1|6|6|
|7|-5|1|6|
|8|4|5|6|

Answer

```text
Maximum Sum = 6
```

---

# Handling All Negative Numbers

Example

```python
arr = [-5,-2,-8,-1]
```

Answer

```text
-1
```

Important:

Initialize

```python
maximum_sum = arr[0]
```

NOT

```python
maximum_sum = 0
```

Otherwise, the algorithm fails for arrays containing only negative numbers.

---

# Complexity

Time

```text
O(n)
```

Space

```text
O(1)
```

---

# Comparison

| Approach | Time | Space |
|----------|------|--------|
| Brute Force | O(n²) | O(1) |
| Kadane's Algorithm | O(n) | O(1) |

---

# Advantages

- Single traversal
- Constant extra space
- Very efficient
- Easy to implement
- Frequently asked in interviews

---

# Common Mistakes

- Initializing `maximum_sum = 0`.
- Resetting `current_sum` before updating `maximum_sum`.
- Confusing subarray with subsequence.
- Forgetting to handle all-negative arrays.

---

# Interview Tips

If the interviewer says:

- Maximum Sum
- Largest Sum
- Contiguous Subarray
- Continuous Elements

Immediately think:

**Kadane's Algorithm**

---

# Pattern Recognition

Use Kadane's Algorithm when:

- You need the maximum sum.
- Elements must be contiguous.
- An O(n) solution is expected.

---

# LeetCode Problems

## 53. Maximum Subarray

Difficulty

Medium

Pattern

Kadane's Algorithm

Status

✅ Solved

---

## Bonus

152. Maximum Product Subarray

Difficulty

Medium

Status

📖 Problem Read

---

# Questions Completed Today

## Local Practice

- Kadane's Algorithm
- Maximum Subarray
- Dry Run Exercises
- Practice Questions
- Interview Questions

## LeetCode

- 53. Maximum Subarray

---

# Key Takeaways

- A subarray must contain consecutive elements.
- Kadane's Algorithm solves the Maximum Subarray problem in O(n).
- Negative running sums are discarded.
- Initialize `maximum_sum` with the first element to handle all-negative arrays.
- Kadane's Algorithm is one of the most important array interview algorithms.

---

# Status

✅ Day 12 Completed