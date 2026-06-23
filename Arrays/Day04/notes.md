# Day 04 - Prefix Sum

## Goal of Day 04

Today I learned:

- Prefix Sum
- Running Sum
- Range Sum Query
- Why Prefix Sum is useful
- Difference between Brute Force and Optimized approaches

---

# 1. Prefix Sum

A Prefix Sum array stores cumulative sums.

Example:

```python
arr = [1,2,3,4,5]
```

Prefix Sum:

```text
[1,3,6,10,15]
```

Explanation:

prefix[0] = 1

prefix[1] = 1 + 2 = 3

prefix[2] = 1 + 2 + 3 = 6

prefix[3] = 1 + 2 + 3 + 4 = 10

prefix[4] = 1 + 2 + 3 + 4 + 5 = 15

---

# Building Prefix Sum Array

```python
arr = [1,2,3,4,5]

running_sum = 0
prefix = []

for num in arr:
    running_sum += num
    prefix.append(running_sum)

print(prefix)
```

Output:

```python
[1,3,6,10,15]
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

# 2. Running Sum

Running Sum means keeping track of the sum seen so far.

Example:

```python
arr = [5,10,15,20]
```

Process:

```text
5

5 + 10 = 15

15 + 15 = 30

30 + 20 = 50
```

Result:

```python
[5,15,30,50]
```

---

# 3. Range Sum Query

Question:

Find sum between two indices.

Example:

```python
arr = [1,2,3,4,5]

left = 1
right = 3
```

Required:

```text
2 + 3 + 4 = 9
```

---

## Brute Force Approach

```python
total = 0

for i in range(left,right+1):
    total += arr[i]
```

Complexity:

```text
O(n)
```

for every query.

---

# 4. Prefix Sum Optimization

Array:

```python
arr = [1,2,3,4,5]
```

Prefix:

```python
[1,3,6,10,15]
```

Formula:

```python
sum(left,right)

=
prefix[right]
-
prefix[left-1]
```

Example:

```python
left = 1
right = 3
```

Calculation:

```python
10 - 1 = 9
```

Answer:

```python
9
```

---

# Why Prefix Sum Is Important?

Suppose:

```text
1000 Range Sum Queries
```

Brute Force:

```text
1000 × O(n)
```

Prefix Sum:

```text
Build Prefix Once -> O(n)

Each Query -> O(1)
```

Much faster.

---

# Complexity Comparison

| Method | Build | Query |
|----------|----------|----------|
| Brute Force | O(1) | O(n) |
| Prefix Sum | O(n) | O(1) |

---

# LeetCode Connections

## 1480. Running Sum of 1D Array

Concept:

- Running Sum
- Prefix Sum Foundation

Complexity:

```text
Time: O(n)
Space: O(n)
```

---

## 303. Range Sum Query - Immutable

Concept:

- Prefix Sum
- Fast Queries

Status:

⏳ To Be Solved

---

# Mistakes To Avoid

Do not use:

```python
sum
```

Use:

```python
running_sum
```

Reason:

sum() is a built-in Python function.

---

# Key Takeaways

- Prefix Sum stores cumulative sums.
- Running Sum is the foundation of Prefix Sum.
- Range Sum Query can be optimized using Prefix Sum.
- Prefix Sum is a common interview pattern.
- Building Prefix Sum takes O(n).
- Query Answering becomes O(1).

---

# Questions Completed Today

## Local Practice

- Prefix Sum Array
- Running Sum
- Range Sum Query

## LeetCode

- 1480. Running Sum of 1D Array (Revision)
- 303. Range Sum Query - Immutable (Pending)

Status:

✅ Day 04 Completed