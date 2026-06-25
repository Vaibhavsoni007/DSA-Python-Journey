# Day 05 - Sliding Window (Fixed Size)

## Goal of Day 05

Today I learned:

- Sliding Window Pattern
- Fixed Size Window
- Maximum Sum Subarray
- Average of Subarrays
- Window Optimization

---

# 1. What is Sliding Window?

Sliding Window is a technique used when we need to process:

- Continuous Subarrays
- Continuous Segments
- Fixed Size Windows

Instead of recalculating everything again and again.

---

# Example

Array:

```python
arr = [1,2,3,4,5]
k = 3
```

Possible windows:

```text
[1,2,3] = 6

[2,3,4] = 9

[3,4,5] = 12
```

Maximum Sum:

```text
12
```

---

# Brute Force Approach

For every window:

1. Calculate sum again.
2. Compare with maximum.

Complexity:

```text
O(n*k)
```

If:

n = 10000

k = 500

This becomes very slow.

---

# Sliding Window Idea

Instead of calculating every window from scratch:

Window 1:

```text
[1,2,3]
Sum = 6
```

Move one step right.

Window 2:

```text
[2,3,4]
```

Instead of:

```text
2+3+4
```

Use previous sum:

```text
6 - 1 + 4 = 9
```

Move again:

```text
9 - 2 + 5 = 12
```

This avoids repeated work.

---

# Sliding Window Formula

```text
New Window Sum

=

Previous Window Sum

- Outgoing Element

+ Incoming Element
```

Python:

```python
window_sum = window_sum + arr[i] - arr[i-k]
```

---

# 2. Maximum Sum Subarray of Size K

Input:

```python
arr = [1,2,3,4,5]
k = 3
```

Windows:

```text
[1,2,3] -> 6

[2,3,4] -> 9

[3,4,5] -> 12
```

Output:

```text
12
```

---

## Algorithm

Step 1:

Calculate first window sum.

```python
window_sum = sum(arr[:k])
```

Step 2:

Store it.

```python
max_sum = window_sum
```

Step 3:

Slide the window.

```python
window_sum = window_sum + arr[i] - arr[i-k]
```

Step 4:

Update maximum.

```python
max_sum = max(max_sum, window_sum)
```

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

# 3. Average of Every Window

Input:

```python
arr = [1,2,3,4,5]
k = 2
```

Windows:

```text
[1,2] -> 1.5

[2,3] -> 2.5

[3,4] -> 3.5

[4,5] -> 4.5
```

Output:

```python
[1.5,2.5,3.5,4.5]
```

---

## Algorithm

First:

```python
window_sum = sum(arr[:k])
```

Store first average.

```python
result.append(window_sum / k)
```

Then slide:

```python
window_sum = window_sum + arr[i] - arr[i-k]
```

Store average.

```python
result.append(window_sum / k)
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

# Fixed Size Window

Today's problems used:

```text
Fixed Window Size
```

Example:

```text
k = 2
k = 3
k = 5
```

Window size never changes.

---

# Why Sliding Window is Important?

Many interview problems ask:

- Maximum Sum Subarray
- Maximum Average Subarray
- Longest Substring
- Longest Unique Characters
- Minimum Size Subarray

Sliding Window is one of the most common interview patterns.

---

# Complexity Comparison

| Approach | Complexity |
|-----------|-----------|
| Brute Force | O(n*k) |
| Sliding Window | O(n) |

---

# LeetCode Connection

## 643. Maximum Average Subarray I

Concept:

```text
Sliding Window
```

Complexity:

```text
Time: O(n)
Space: O(1)
```

Status:

⏳ To Be Solved

---

# Mistakes to Avoid

Avoid recalculating window sums repeatedly.

Bad:

```python
sum(arr[i:i+k])
```

inside every loop.

Reason:

```text
O(n*k)
```

Use Sliding Window instead.

---

# Key Takeaways

- Sliding Window is used for continuous subarrays.
- Fixed Size Window keeps k constant.
- Reuse previous calculations.
- New Window = Old Window - Outgoing + Incoming.
- Sliding Window often reduces O(n*k) to O(n).
- It is one of the most important interview patterns.

---

# Questions Completed Today

## Local Practice

- Maximum Sum Subarray
- Average of Subarrays
- Sliding Window Practice

## LeetCode

- 643. Maximum Average Subarray I (Pending)

Status:

✅ Day 05 Completed