# Day 16 - Trapping Rain Water

## Goal of Day 16

Today I learned:

- What is the Trapping Rain Water problem?
- Brute Force Approach
- Prefix Maximum Array
- Suffix Maximum Array
- Two Pointer Approach
- Water Trapping Formula
- Time & Space Complexity
- Pattern Recognition

---

# Problem Statement

Given an array where each element represents the height of a building,

calculate how many units of water can be trapped after rainfall.

Example

```python
height = [0,1,0,2,1,0,1,3,2,1,2,1]
```

Output

```text
6
```

---

# Visual Understanding

Example

```python
height = [3,0,2]
```

Visualization

```
█     █
█  ~  █
█  ~  █
---------
3  0  2
```

Water gets trapped because both sides have taller buildings.

---

# Observation

At every index,

the trapped water depends on

- Maximum height on the left
- Maximum height on the right

Formula

```
Water at index

=

min(leftMax, rightMax)

-

height[i]
```

If the answer becomes negative,

consider it **0**.

---

# Example

```python
height = [3,0,2]
```

Current Height

```
0
```

Left Maximum

```
3
```

Right Maximum

```
2
```

Water

```
min(3,2) - 0

=

2
```

So,

2 units of water are trapped.

---

# Brute Force Approach

For every index

Find

- Left Maximum
- Right Maximum

Then

```
water += min(leftMax,rightMax)-height[i]
```

Pseudo Code

```
for every index

    leftMax = maximum element on left

    rightMax = maximum element on right

    water += min(leftMax,rightMax)-height[i]
```

---

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

but is slow for large arrays.

---

# Prefix Maximum Array

Store the highest building seen so far from the left.

Example

```python
height = [0,1,0,2,1]
```

Left Maximum Array

```
[0,1,1,2,2]
```

Meaning

```
leftMax[i]

=

maximum height from index 0 to i
```

---

# Suffix Maximum Array

Store the highest building seen so far from the right.

Example

```python
height = [0,1,0,2,1]
```

Right Maximum Array

```
[2,2,2,2,1]
```

Meaning

```
rightMax[i]

=

maximum height from index i to last index
```

---

# Prefix + Suffix Solution

For every index

```
water

=

min(leftMax[i], rightMax[i])

-

height[i]
```

Add all water values.

---

## Dry Run

Input

```python
height = [4,2,0,3,2,5]
```

| Index | Height | LeftMax | RightMax | Water |
|------|--------|---------|----------|-------|
|0|4|4|5|0|
|1|2|4|5|2|
|2|0|4|5|4|
|3|3|4|5|1|
|4|2|4|5|2|
|5|5|5|5|0|

Total Water

```
9
```

---

# Two Pointer Approach

Instead of storing two arrays,

use

```
left

right

leftMax

rightMax
```

Algorithm

- Start with two pointers.
- Update leftMax and rightMax while moving inward.
- Move the pointer having the smaller height.
- Calculate trapped water on the fly.

This removes the need for extra arrays.

---

## Why move the smaller pointer?

Water level depends on the smaller boundary.

If

```
height[left] < height[right]
```

then the left side decides the maximum water that can be trapped.

Similarly,

if the right height is smaller,

move the right pointer.

---

# Complexity Comparison

| Approach | Time | Space |
|----------|------|--------|
| Brute Force | O(n²) | O(1) |
| Prefix + Suffix | O(n) | O(n) |
| Two Pointer | O(n) | O(1) |

---

# Advantages of Two Pointer Approach

- Linear time.
- Constant extra space.
- No additional arrays required.
- Preferred in interviews.

---

# Common Mistakes

- Using `max(leftMax,rightMax)` instead of `min(...)`.
- Forgetting to update leftMax/rightMax.
- Adding negative water values.
- Moving the wrong pointer.
- Ignoring arrays with length less than 3.

---

# Interview Tips

Whenever you hear

- Rain Water
- Heights
- Left Boundary
- Right Boundary
- Trapped Water

Immediately think

**Prefix Maximum + Suffix Maximum**

then optimize using

**Two Pointers**

---

# Pattern Recognition

This pattern is useful when

- Both left and right information are required.
- Prefix and suffix values can be precomputed.
- Extra space can later be optimized using two pointers.

---

# LeetCode Problems

## 42. Trapping Rain Water

Difficulty

Hard

Pattern

Prefix Maximum

Suffix Maximum

Two Pointers

Status

✅ Solved

---

## Bonus Reading

11. Container With Most Water

Difficulty

Medium

Status

📖 Problem Read

---

# Questions Completed Today

## Local Practice

- Brute Force
- Prefix Maximum
- Suffix Maximum
- Two Pointer Approach
- Practice Questions
- Interview Questions

## LeetCode

- 42. Trapping Rain Water

---

# Key Takeaways

- Water depends on the smaller boundary.
- Formula:

```
min(leftMax,rightMax) - height[i]
```

- Prefix and Suffix arrays reduce complexity to O(n).
- Two Pointer Approach further reduces space to O(1).
- This is one of the most important Hard interview problems.

---

# Status

✅ Day 16 Completed