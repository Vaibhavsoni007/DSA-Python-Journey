# Day 11 - Dutch National Flag Algorithm (Three Pointers)

## Goal of Day 11

Today I learned:

- Dutch National Flag Algorithm
- Three Pointer Technique
- Sorting an Array of 0s, 1s and 2s
- In-place Array Rearrangement
- Interview Approach for LeetCode 75

---

# What is the Dutch National Flag Algorithm?

The Dutch National Flag Algorithm is an efficient algorithm used to sort an array containing only three distinct values.

Example:

```python
arr = [2,0,2,1,1,0]
```

Output

```python
[0,0,1,1,2,2]
```

Instead of using Bubble Sort (O(n²)), this algorithm sorts the array in a single traversal.

---

# Why is it Called Dutch National Flag?

The Dutch flag has three horizontal colors:

- Red
- White
- Blue

Similarly, our array contains three different values:

```text
0
1
2
```

The algorithm separates these three groups efficiently.

---

# Why Not Bubble Sort?

Bubble Sort

Time Complexity

```text
O(n²)
```

Dutch National Flag

Time Complexity

```text
O(n)
```

Single traversal.

No nested loops.

---

# Three Pointer Technique

Maintain three pointers.

```python
low = 0
mid = 0
high = len(arr) - 1
```

Each pointer has a specific role.

---

# Pointer Meaning

## Before low

All elements are

```text
0
```

---

## Between low and mid-1

All elements are

```text
1
```

---

## Between mid and high

Unknown elements.

Need processing.

---

## After high

All elements are

```text
2
```

---

# Algorithm

Continue while

```python
mid <= high
```

---

## Case 1

If

```python
arr[mid] == 0
```

Swap

```python
arr[low]
arr[mid]
```

Move

```python
low += 1
mid += 1
```

Reason:

The element placed at mid has already been processed.

---

## Case 2

If

```python
arr[mid] == 1
```

Simply move

```python
mid += 1
```

Reason:

1 already belongs to the middle section.

---

## Case 3

If

```python
arr[mid] == 2
```

Swap

```python
arr[mid]
arr[high]
```

Move

```python
high -= 1
```

Do NOT increase mid.

Reason:

The element that came from the right side has not been processed yet.

---

# Dry Run

Example

```python
arr = [2,0,2,1,1,0]
```

Initial

```text
low = 0
mid = 0
high = 5
```

Process

```text
2 found

Swap with high

↓

0 0 2 1 1 2
```

Now

```text
high = 4

mid remains 0
```

Continue until

```text
mid > high
```

Final

```text
0 0 1 1 2 2
```

---

# Why Don't We Increment mid After Swapping with high?

Suppose

```text
2 0 1
```

After swapping

```text
1 0 2
```

The new value at index mid has never been checked.

If we increase mid immediately,

we may skip processing that element.

Therefore,

```text
Only decrease high.

Keep mid unchanged.
```

---

# Complexity

Time

```text
O(n)
```

Every element is processed at most once.

---

Space

```text
O(1)
```

Only three pointers are used.

---

# Comparison

| Algorithm | Time | Space |
|-----------|------|--------|
| Bubble Sort | O(n²) | O(1) |
| Counting Method | O(n) | O(1) |
| Dutch National Flag | O(n) | O(1) |

---

# Advantages

- Single traversal
- No extra array
- In-place sorting
- Excellent interview question
- Very efficient

---

# Common Mistakes

- Incrementing mid after swapping with high.
- Using nested loops.
- Forgetting the condition:

```python
while mid <= high
```

- Mixing up the roles of low, mid and high.

---

# Interview Tips

If the interviewer says:

"Sort an array containing only 0s, 1s and 2s."

Think immediately about:

Dutch National Flag Algorithm.

If the interviewer asks:

"Can you solve it in one traversal?"

Answer:

Yes.

Use three pointers.

---

# Pattern Recognition

Think about this algorithm when:

- Array contains only a few distinct values.
- In-place sorting is required.
- Single traversal is expected.
- Constant extra space is required.

---

# LeetCode Problems

## 75. Sort Colors

Difficulty

Medium

Pattern

Three Pointers

Status

✅ Solved

---

## Bonus

905. Sort Array By Parity

Difficulty

Easy

Pattern

Two Pointers

Status

✅ Practiced

---

# Questions Completed Today

## Local Practice

- Dutch National Flag Algorithm
- Three Pointer Implementation
- Practice Questions
- Interview Questions
- Dry Run Exercises

## LeetCode

- 75. Sort Colors
- 905. Sort Array By Parity (Bonus)

---

# Key Takeaways

- Three pointers divide the array into processed and unprocessed regions.
- The algorithm sorts the array in one traversal.
- No extra memory is required.
- Never increment mid after swapping with high.
- This is one of the most frequently asked array interview algorithms.

---

# Status

✅ Day 11 Completed