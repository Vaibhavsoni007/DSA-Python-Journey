# Day 09 - Variable Size Sliding Window

## Goal of Day 09

Today I learned:

- Variable Size Sliding Window
- Window Expansion
- Window Shrinking
- Longest Subarray with Sum ≤ K
- Sliding Window Template
- Interview Pattern Recognition

---

# What is Variable Size Sliding Window?

Variable Size Sliding Window is an optimization technique where the window size changes dynamically based on a condition.

Unlike Fixed Size Sliding Window, the window is allowed to expand and shrink.

It is commonly used in:

- Longest Subarray Problems
- Shortest Subarray Problems
- Substring Problems
- Frequency Based Problems
- HashMap + Sliding Window Problems

---

# Fixed Window vs Variable Window

| Fixed Window | Variable Window |
|--------------|-----------------|
| Window size is fixed | Window size changes dynamically |
| Given value of K | No fixed window size |
| Easy implementation | Slightly more complex |
| Example: Maximum Sum of Size K | Example: Minimum Size Subarray |

---

# Two Pointer Technique

Variable Sliding Window uses two pointers.

```python
left = 0
right = 0
```

Purpose of pointers:

- left → Shrinks the window
- right → Expands the window

---

# General Algorithm

Step 1

Expand the window.

```python
window_sum += arr[right]
```

---

Step 2

Check the condition.

Example:

```python
window_sum > k
```

---

Step 3

If condition breaks,

Shrink the window.

```python
window_sum -= arr[left]
left += 1
```

---

Step 4

Update the answer.

```python
answer = max(answer, right - left + 1)
```

---

# Dry Run

Example

```python
arr = [1,2,1,0,1,1,0]
k = 4
```

Initial

```text
Left = 0
Right = 0
Sum = 0
```

Expand

```text
Window = [1]
Sum = 1
```

Expand

```text
Window = [1,2]
Sum = 3
```

Expand

```text
Window = [1,2,1]
Sum = 4
```

Expand

```text
Window = [1,2,1,0]
Sum = 4
```

Expand

```text
Window = [1,2,1,0,1]
Sum = 5
```

Condition breaks.

Shrink.

```text
Remove 1

Window = [2,1,0,1]

Sum = 4
```

Continue...

---

# Sliding Window Template

```python
left = 0
window_sum = 0

for right in range(len(arr)):

    window_sum += arr[right]

    while window_sum > k:

        window_sum -= arr[left]
        left += 1

    answer = max(answer, right-left+1)
```

---

# Why is this O(n)?

At first glance it looks like two loops.

But actually,

- right moves only forward.
- left also moves only forward.

Each pointer visits every element at most once.

Therefore,

Time Complexity:

```text
O(n)
```

Space Complexity:

```text
O(1)
```

---

# Common Interview Problems

Variable Sliding Window is used in:

- Minimum Size Subarray Sum
- Longest Substring Without Repeating Characters
- Fruits Into Baskets
- Longest Repeating Character Replacement
- Maximum Consecutive Ones
- Minimum Window Substring

---

# LeetCode Problems

## 209. Minimum Size Subarray Sum

Difficulty:

Medium

Pattern:

Variable Sliding Window

Status:

✅ Solved

---

## 3. Longest Substring Without Repeating Characters

Difficulty:

Medium

Pattern:

Sliding Window + HashMap

Status:

✅ Solved

---

# Common Mistakes

- Forgetting to shrink the window.
- Updating the answer before satisfying the condition.
- Moving the wrong pointer.
- Using nested loops unnecessarily.
- Forgetting that both pointers only move forward.

---

# Pattern Recognition

Think about Variable Sliding Window when you see:

- Longest
- Smallest
- Minimum Length
- Maximum Length
- Continuous Subarray
- Continuous Substring
- At Most K
- At Least K

---

# Complexity

| Operation | Complexity |
|-----------|------------|
| Time | O(n) |
| Space | O(1) |

---

# Questions Completed Today

## Local Practice

- Variable Window Introduction
- Longest Subarray with Sum ≤ K
- Practice Questions
- Interview Questions

## LeetCode

- 209. Minimum Size Subarray Sum
- 3. Longest Substring Without Repeating Characters

Status:

✅ Day 09 Completed

---

# Key Takeaways

- Variable Sliding Window is an extension of Fixed Window.
- Window size changes dynamically.
- Two pointers are used to expand and shrink the window.
- Every element is processed at most twice.
- Time Complexity remains O(n).
- One of the most important interview patterns for Arrays and Strings.