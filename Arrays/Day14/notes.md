# Day 14 - Array Rotation (Reversal Algorithm)

## Goal of Day 14

Today I learned:

- What is Array Rotation?
- Left Rotation
- Right Rotation
- Rotation by K Positions
- Brute Force Approach
- Extra Array Approach
- Reversal Algorithm
- Time & Space Complexity

---

# What is Array Rotation?

Array rotation means shifting every element of an array either to the left or to the right.

There are two types:

- Left Rotation
- Right Rotation

---

# Left Rotation

Example

```python
arr = [1,2,3,4,5]
k = 1
```

Output

```text
[2,3,4,5,1]
```

The first element moves to the end.

---

# Right Rotation

Example

```python
arr = [1,2,3,4,5]
k = 1
```

Output

```text
[5,1,2,3,4]
```

The last element moves to the front.

---

# Rotation by K Positions

Example

```python
arr = [1,2,3,4,5,6,7]
k = 3
```

Right Rotation

```text
[5,6,7,1,2,3,4]
```

Left Rotation

```text
[4,5,6,7,1,2,3]
```

---

# Why do we calculate k % n?

If k is greater than the array length, rotating k times is the same as rotating (k % n) times.

Example

```python
arr = [1,2,3,4,5]
k = 8
```

Length = 5

```text
8 % 5 = 3
```

So rotating 8 times is equivalent to rotating 3 times.

---

# Brute Force Approach

Rotate the array one step at a time.

Repeat this process k times.

## Complexity

Time

```text
O(n × k)
```

Space

```text
O(1)
```

Simple to understand but inefficient for large values of k.

---

# Extra Array Approach

Create another array.

Place each element at its new position.

## Complexity

Time

```text
O(n)
```

Space

```text
O(n)
```

Easy to implement but requires extra memory.

---

# Reversal Algorithm

This is the optimal approach.

### Steps for Right Rotation

Example

```python
arr = [1,2,3,4,5,6,7]
k = 3
```

Step 1

Reverse the complete array

```text
7 6 5 4 3 2 1
```

Step 2

Reverse first k elements

```text
5 6 7 4 3 2 1
```

Step 3

Reverse remaining elements

```text
5 6 7 1 2 3 4
```

Final Answer

```text
[5,6,7,1,2,3,4]
```

---

# Dry Run

Input

```python
arr = [1,2,3,4,5,6]
k = 2
```

| Step | Array |
|------|-------|
|Original|1 2 3 4 5 6|
|Reverse All|6 5 4 3 2 1|
|Reverse First k|5 6 4 3 2 1|
|Reverse Remaining|5 6 1 2 3 4|

Answer

```text
[5,6,1,2,3,4]
```

---

# Complexity Comparison

| Approach | Time | Space |
|----------|------|--------|
| Brute Force | O(n × k) | O(1) |
| Extra Array | O(n) | O(n) |
| Reversal Algorithm | O(n) | O(1) |

---

# Advantages of Reversal Algorithm

- Runs in linear time.
- Uses constant extra space.
- Performs rotation in-place.
- Preferred in coding interviews.

---

# Common Mistakes

- Forgetting to calculate `k = k % len(arr)`.
- Incorrect reversal ranges.
- Confusing left rotation with right rotation.
- Not handling empty arrays.
- Not handling arrays with one element.

---

# Interview Tips

Whenever you hear:

- Rotate Array
- Rotate by k Positions
- Circular Shift
- In-place Rotation

Think of the **Reversal Algorithm**.

---

# Pattern Recognition

Use this algorithm when:

- Rotation must be done in-place.
- O(1) extra space is required.
- Large arrays need efficient rotation.

---

# LeetCode Problems

## 189. Rotate Array

Difficulty

Medium

Pattern

Array Rotation

Reversal Algorithm

Status

✅ Solved

---

## Bonus

1752. Check if Array Is Sorted and Rotated

Difficulty

Easy

Status

📖 Problem Read / Attempted

---

# Questions Completed Today

## Local Practice

- Left Rotation
- Right Rotation
- Reversal Algorithm
- Practice Questions
- Interview Questions

## LeetCode

- 189. Rotate Array

---

# Key Takeaways

- Arrays can be rotated left or right.
- Always calculate `k = k % n`.
- Reversal Algorithm is the optimal solution.
- Reversal Algorithm runs in O(n) time and O(1) space.
- This is a frequently asked interview topic.

---

# Status

✅ Day 14 Completed