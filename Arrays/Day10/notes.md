# Day 10 - Sorting Fundamentals

## Goal of Day 10

Today I learned:

- What is Sorting?
- Bubble Sort
- Selection Sort
- Insertion Sort
- Stable vs Unstable Sorting
- In-place vs Out-of-place Sorting
- Time & Space Complexity Comparison

---

# What is Sorting?

Sorting means arranging data in a specific order.

Two common orders are:

Ascending Order

```python
[8,3,5,1]

↓

[1,3,5,8]
```

Descending Order

```python
[8,5,3,1]
```

---

# Why Do We Need Sorting?

Sorting helps in:

- Faster Searching (Binary Search)
- Duplicate Detection
- Data Analysis
- Efficient Merging
- Interview Problems
- Database Operations

---

# Bubble Sort

## Idea

Compare adjacent elements.

If they are in the wrong order,

swap them.

After every pass,

the largest element moves to the end.

Example

```text
5 2 4 1

↓

2 5 4 1

↓

2 4 5 1

↓

2 4 1 5
```

Largest element has reached its correct position.

---

## Algorithm

Repeat (n-1) passes.

For every adjacent pair:

```python
if arr[j] > arr[j+1]:
    swap
```

---

## Complexity

Best Case

O(n)

(when optimized using swapped flag)

Average Case

O(n²)

Worst Case

O(n²)

Space

O(1)

Stable

✅ Yes

In-place

✅ Yes

---

# Bubble Sort Optimization

If during a complete pass no swaps occur,

the array is already sorted.

Use a boolean variable:

```python
swapped = False
```

If no swap occurs,

stop early.

This improves the best-case complexity to O(n).

---

# Selection Sort

## Idea

Find the minimum element.

Place it at the beginning.

Repeat for the remaining array.

Example

```text
7 4 9 2

↓

2 4 9 7

↓

2 4 9 7

↓

2 4 7 9
```

---

## Complexity

Best Case

O(n²)

Average Case

O(n²)

Worst Case

O(n²)

Space

O(1)

Stable

❌ No

In-place

✅ Yes

---

# Why is Selection Sort Unstable?

Consider:

```text
5A 3 5B 2
```

After swapping,

```text
2 3 5B 5A
```

The relative order of equal elements changes.

Hence,

Selection Sort is unstable.

---

# Insertion Sort

## Idea

Divide the array into:

- Sorted Part
- Unsorted Part

Pick one element from the unsorted part and insert it into its correct position.

Example

```text
5 3 4 1

↓

3 5 4 1

↓

3 4 5 1

↓

1 3 4 5
```

---

## Complexity

Best Case

O(n)

Average Case

O(n²)

Worst Case

O(n²)

Space

O(1)

Stable

✅ Yes

In-place

✅ Yes

---

# Why is Insertion Sort Fast on Nearly Sorted Arrays?

If the array is almost sorted,

very few shifts are required.

Therefore,

Insertion Sort performs close to O(n).

This makes it useful for:

- Small datasets
- Nearly sorted data

---

# Stable vs Unstable Sorting

Stable Sorting

Equal elements keep their original order.

Example

```text
5A 3 5B

↓

3 5A 5B
```

Examples

- Bubble Sort
- Insertion Sort
- Merge Sort

---

Unstable Sorting

Equal elements may change their order.

Examples

- Selection Sort
- Quick Sort (default implementation)
- Heap Sort

---

# In-place vs Out-of-place

In-place

Uses only constant extra memory.

Examples

- Bubble Sort
- Selection Sort
- Insertion Sort

Space

O(1)

---

Out-of-place

Requires an additional array.

Examples

- Merge Sort

Space

O(n)

---

# Complexity Comparison

| Algorithm | Best | Average | Worst | Space | Stable | In-place |
|-----------|------|---------|--------|--------|---------|----------|
| Bubble Sort | O(n)* | O(n²) | O(n²) | O(1) | ✅ | ✅ |
| Selection Sort | O(n²) | O(n²) | O(n²) | O(1) | ❌ | ✅ |
| Insertion Sort | O(n) | O(n²) | O(n²) | O(1) | ✅ | ✅ |

*Best case only with optimization.

---

# When Should We Use Each?

Bubble Sort

- Educational purposes
- Learning swapping

Selection Sort

- When minimizing swaps is important

Insertion Sort

- Small arrays
- Nearly sorted arrays

---

# Common Mistakes

- Forgetting loop boundaries.
- Incorrect swapping.
- Missing the optimization in Bubble Sort.
- Forgetting to shift elements in Insertion Sort.
- Assuming Selection Sort is stable.

---

# Interview Tips

If asked:

"Which sorting algorithm is best for a nearly sorted array?"

Answer:

Insertion Sort.

If asked:

"Which algorithm performs the fewest swaps?"

Answer:

Selection Sort.

If asked:

"Why is Bubble Sort rarely used in production?"

Answer:

Its average and worst-case complexity is O(n²), making it inefficient for large datasets.

---

# Questions Completed Today

## Local Practice

- Bubble Sort
- Selection Sort
- Insertion Sort
- Practice Questions
- Interview Questions

## LeetCode

- 912. Sort an Array (learning implementation)
- 75. Sort Colors (problem analysis)

Status:

✅ Day 10 Completed

---

# Key Takeaways

- Sorting arranges data in a meaningful order.
- Bubble Sort repeatedly swaps adjacent elements.
- Selection Sort selects the minimum element in each pass.
- Insertion Sort inserts elements into the correct position.
- Stable sorting preserves the order of equal elements.
- In-place algorithms require only constant extra space.
- Insertion Sort is efficient for small or nearly sorted datasets.