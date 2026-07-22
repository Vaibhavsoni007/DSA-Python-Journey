# Day 17 - Container With Most Water

## Goal of Day 17

Today I learned:

- What is the Container With Most Water problem?
- Brute Force Approach
- Two Pointer Approach
- Area Formula
- Why We Move the Smaller Pointer
- Time & Space Complexity
- Pattern Recognition

---

# Problem Statement

Given an array `height`, where each element represents the height of a vertical line, find two lines that together with the x-axis form a container that can hold the maximum amount of water.

Return the maximum area.

---

# Example

```python
height = [1,8,6,2,5,4,8,3,7]
```

Output

```text
49
```

Explanation

Choose

```
height = 8

and

height = 7
```

Width

```
8 - 1 = 7
```

Area

```
7 × 7 = 49
```

---

# Area Formula

Area depends on two things:

- Width
- Smaller Height

Formula

```
Area

=

min(height[left], height[right])

×

(right-left)
```

---

# Why Minimum Height?

Suppose

```
Left = 4

Right = 9
```

Water cannot rise above the shorter wall.

Therefore

```
Area

=

4 × Width
```

NOT

```
9 × Width
```

The smaller wall always limits the water level.

---

# Brute Force Approach

Check every possible pair.

Pseudo Code

```
maximum = 0

for i

    for j

        area = min(height[i],height[j])

               ×

               (j-i)

        maximum = max(maximum,area)
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

Correct,

but inefficient.

---

# Two Pointer Approach

Initialize

```
left = 0

right = n-1
```

Steps

1. Calculate current area.
2. Update maximum area.
3. Move the pointer having the smaller height.
4. Continue until left >= right.

---

# Why Move the Smaller Pointer?

Suppose

```
Left Height = 3

Right Height = 8
```

Current Area

```
3 × Width
```

Moving the taller pointer only decreases the width while the smaller height (3) still limits the area.

The only chance to increase the area is to move the smaller pointer and hope to find a taller line.

This is the key idea behind the optimal solution.

---

# Dry Run

Input

```python
height = [1,8,6,2,5]
```

| Left | Right | Width | Min Height | Area | Maximum |
|------|-------|-------|------------|------|---------|
|0|4|4|1|4|4|
|1|4|3|5|15|15|
|1|3|2|2|4|15|
|1|2|1|6|6|15|

Final Answer

```
15
```

---

# Complexity Comparison

| Approach | Time | Space |
|----------|------|--------|
| Brute Force | O(n²) | O(1) |
| Two Pointer | O(n) | O(1) |

---

# Advantages of Two Pointer Approach

- Linear time complexity.
- Constant extra space.
- Single traversal.
- Preferred in coding interviews.

---

# Comparison with Trapping Rain Water

| Container With Most Water | Trapping Rain Water |
|---------------------------|---------------------|
| Find one maximum area | Find total trapped water |
| Area = Width × Minimum Height | Water = min(leftMax, rightMax) - height[i] |
| Move smaller pointer | Maintain leftMax/rightMax while moving pointers |
| Return maximum area | Return total water |

Although both use Two Pointers, their goals and formulas are different.

---

# Common Mistakes

- Using maximum height instead of minimum height.
- Moving the taller pointer.
- Forgetting to update the maximum area.
- Incorrect width calculation.
- Stopping before left >= right.

---

# Interview Tips

Whenever you hear

- Maximum Area
- Two Vertical Lines
- Width × Height
- Container

Immediately think

**Two Pointer Technique**

---

# Pattern Recognition

Use this pattern when

- Two ends of the array are involved.
- Width changes gradually.
- A linear solution is expected.
- The problem asks for a maximum or minimum value.

---

# LeetCode Problems

## 11. Container With Most Water

Difficulty

Medium

Pattern

Two Pointers

Status

✅ Solved

---

## Bonus

167. Two Sum II – Input Array Is Sorted

Difficulty

Medium

Status

📖 Problem Read / Attempted

---

# Questions Completed Today

## Local Practice

- Brute Force Solution
- Two Pointer Solution
- Dry Runs
- Practice Questions
- Interview Questions

## LeetCode

- 11. Container With Most Water

---

# Key Takeaways

- Area depends on the smaller height.
- Formula:

```
Area = min(height[left], height[right]) × (right - left)
```

- Move the pointer with the smaller height.
- Optimal solution runs in O(n) time and O(1) space.
- This is one of the most frequently asked Two Pointer interview problems.

---

# Status

✅ Day 17 Completed