# Day 06 - Binary Search

## Goal of Day 06

Today I learned:

- Binary Search
- Searching in Sorted Arrays
- Binary Search Algorithm
- Time Complexity Analysis
- Search Insert Position

---

# 1. What is Binary Search?

Binary Search is an efficient searching algorithm.

Instead of checking every element, it repeatedly divides the search space into two halves.

Important:

Binary Search works only on **sorted arrays**.

---

# Example

```python
arr = [2,5,8,12,16,23,38,56,72]
target = 23
```

Search Process:

```text
Middle = 16

23 > 16

Discard Left Half

Remaining:

23 38 56 72
```

Again:

```text
Middle = 38

23 < 38

Discard Right Half
```

Remaining:

```text
23
```

Found.

---

# Binary Search Algorithm

Step 1

```python
left = 0
right = len(arr)-1
```

Step 2

Repeat while:

```python
left <= right
```

Step 3

Find middle.

```python
mid = (left + right)//2
```

Step 4

Compare.

```python
arr[mid] == target
```

Found.

```python
arr[mid] < target
```

Move right.

```python
left = mid + 1
```

```python
arr[mid] > target
```

Move left.

```python
right = mid - 1
```

---

# Dry Run

Array

```python
[2,5,8,12,16,23,38,56,72]
```

Target

```python
23
```

Iteration 1

```text
Left = 0

Right = 8

Mid = 4

Value = 16
```

Go Right.

Iteration 2

```text
Left = 5

Right = 8

Mid = 6

Value = 38
```

Go Left.

Iteration 3

```text
Left = 5

Right = 5

Mid = 5

Value = 23
```

Found.

---

# Complexity

## Linear Search

Time

```text
O(n)
```

---

## Binary Search

Time

```text
O(log n)
```

Space

```text
O(1)
```

---

# Why is Binary Search Faster?

Every iteration removes half of the remaining elements.

Example:

```text
100 Elements

↓

50

↓

25

↓

12

↓

6

↓

3

↓

1
```

Very few comparisons are needed.

---

# Search Insert Position

Question:

Return the index if the target exists.

Otherwise return the position where it should be inserted.

Example:

```python
nums = [1,3,5,6]
target = 2
```

Answer

```text
1
```

---

# Important Observation

After Binary Search ends:

```python
left
```

points to the correct insertion position.

Therefore,

```python
return left
```

is the preferred solution.

---

# LeetCode

## 704. Binary Search

Concepts:

- Binary Search
- Sorted Array

Complexity

```text
Time: O(log n)

Space: O(1)
```

Status

✅ Solved

---

## 35. Search Insert Position

Concepts:

- Binary Search
- Insertion Position

Complexity

```text
Time: O(log n)

Space: O(1)
```

Status

✅ Solved

---

# Mistakes to Avoid

- Applying Binary Search on an unsorted array.
- Updating the wrong pointer (`left` or `right`).
- Incorrect loop condition (`left <= right` is important).
- Returning `mid` after the loop ends instead of the correct insertion position (`left`) when solving insertion problems.

---

# Key Takeaways

- Binary Search works only on sorted arrays.
- Search space is reduced by half every iteration.
- Time Complexity is O(log n).
- Space Complexity is O(1).
- Binary Search is one of the most common interview algorithms.

---

# Questions Completed Today

## Local Practice

- Binary Search
- Binary Search Practice
- Recursive Binary Search (Introduction)

## LeetCode

- 704. Binary Search
- 35. Search Insert Position

Status:

✅ Day 06 Completed