# Day 07 - Binary Search Variations

## Goal of Day 07

Today I learned:

- First Occurrence
- Last Occurrence
- Count Occurrences
- Lower Bound (Concept)
- Upper Bound (Concept)
- Binary Search Variations
- Interview Problems based on Binary Search

---

# Revision: Binary Search

Binary Search works only on **sorted arrays**.

Instead of searching every element, it repeatedly divides the search space into two halves.

Time Complexity:

```text
O(log n)
```

Space Complexity:

```text
O(1)
```

---

# 1. First Occurrence

Problem:

Find the first occurrence of a target in a sorted array containing duplicate values.

Example:

```python
arr = [1,2,2,2,3,4]
target = 2
```

Output:

```text
1
```

---

## Logic

When target is found:

- Store the current index.
- Continue searching on the left side.

```python
answer = mid
right = mid - 1
```

---

## Complexity

Time:

```text
O(log n)
```

Space:

```text
O(1)
```

---

# 2. Last Occurrence

Problem:

Find the last occurrence of a target.

Example:

```python
arr = [1,2,2,2,3,4]
target = 2
```

Output:

```text
3
```

---

## Logic

When target is found:

- Store the current index.
- Continue searching on the right side.

```python
answer = mid
left = mid + 1
```

---

## Complexity

Time:

```text
O(log n)
```

Space:

```text
O(1)
```

---

# 3. Count Occurrences

Once first and last occurrence are known:

Formula:

```text
Count = Last - First + 1
```

Example:

```text
First = 1
Last = 3

Count = 3
```

---

## Complexity

Time:

```text
O(log n)
```

---

# 4. Lower Bound (Concept)

Lower Bound is the first position where:

```text
Element >= Target
```

Example:

```python
arr = [1,2,4,4,5,7]
target = 4
```

Lower Bound:

```text
2
```

---

# 5. Upper Bound (Concept)

Upper Bound is the first position where:

```text
Element > Target
```

Example:

```python
arr = [1,2,4,4,5,7]
target = 4
```

Upper Bound:

```text
4
```

---

# Difference

| Operation | Condition |
|-----------|-----------|
| Lower Bound | First element >= Target |
| Upper Bound | First element > Target |

---

# Binary Search Template

```python
left = 0
right = len(arr) - 1

while left <= right:

    mid = (left + right) // 2

    if arr[mid] == target:
        # process

    elif arr[mid] < target:
        left = mid + 1

    else:
        right = mid - 1
```

---

# Common Interview Tricks

## First Occurrence

```python
right = mid - 1
```

after storing answer.

---

## Last Occurrence

```python
left = mid + 1
```

after storing answer.

---

## Search Insert Position

After loop ends:

```python
return left
```

---

# Edge Cases

Always test Binary Search for:

- Empty Array
- Single Element
- Target Not Present
- Target at First Index
- Target at Last Index
- Duplicate Values
- All Elements Same

---

# Interview Questions Solved

- Binary Search
- Search Insert Position
- First Occurrence
- Last Occurrence
- Count Occurrence

---

# LeetCode Problems

## 34. Find First and Last Position of Element in Sorted Array

Pattern:

- Binary Search
- First Occurrence
- Last Occurrence

Difficulty:

```text
Medium
```

Status:

✅ Solved

---

## 744. Find Smallest Letter Greater Than Target

Pattern:

- Binary Search

Difficulty:

```text
Easy
```

Status:

✅ Solved

---

## 278. First Bad Version

Pattern:

- Binary Search

Difficulty:

```text
Easy
```

Status:

✅ Solved

---

# Complexity Comparison

| Problem | Time | Space |
|---------|------|--------|
| Binary Search | O(log n) | O(1) |
| First Occurrence | O(log n) | O(1) |
| Last Occurrence | O(log n) | O(1) |
| Count Occurrence | O(log n) | O(1) |

---

# Mistakes to Avoid

- Using Binary Search on an unsorted array.
- Forgetting to continue searching after finding the target.
- Returning immediately instead of finding the first or last occurrence.
- Ignoring edge cases like empty arrays and duplicates.

---

# Key Takeaways

- Binary Search reduces the search space by half in each iteration.
- First and Last Occurrence are small modifications of Binary Search.
- Count Occurrence is calculated using First and Last Occurrence.
- Lower Bound and Upper Bound are advanced Binary Search concepts.
- Binary Search is one of the most frequently asked interview algorithms.

---

# Questions Completed Today

## Local Practice

- First Occurrence
- Last Occurrence
- Count Occurrence
- Binary Search Edge Cases
- Interview Practice Questions

## LeetCode

- 34. Find First and Last Position of Element in Sorted Array
- 744. Find Smallest Letter Greater Than Target
- 278. First Bad Version

Status:

✅ Day 07 Completed