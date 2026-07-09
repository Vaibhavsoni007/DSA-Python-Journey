# Day 13 - Moore's Voting Algorithm (Majority Element)

## Goal of Day 13

Today I learned:

- What is a Majority Element?
- Brute Force Approach
- HashMap Approach
- Moore's Voting Algorithm
- Pair Cancellation Concept
- Candidate Selection
- Verification Pass
- Time & Space Complexity

---

# What is a Majority Element?

A majority element is an element that appears **more than n/2 times** in an array.

Example

```python
arr = [2,2,1,1,1,2,2]
```

Length = 7

Majority Condition

```text
Frequency > 7/2 = 3.5

Therefore,

Frequency >= 4
```

Frequency

```text
2 → 4 Times ✅

1 → 3 Times
```

Answer

```text
2
```

---

# Brute Force Approach

For every element,

count its frequency by traversing the entire array.

If frequency > n/2,

return that element.

---

## Complexity

Time

```text
O(n²)
```

Space

```text
O(1)
```

Works correctly,

but inefficient for large arrays.

---

# HashMap Approach

Store frequency of every element.

```python
freq = {}

for num in arr:
    freq[num] = freq.get(num,0) + 1
```

After counting,

check

```python
count > n//2
```

---

## Complexity

Time

```text
O(n)
```

Space

```text
O(n)
```

Better than brute force,

but uses extra memory.

---

# Moore's Voting Algorithm

## Main Idea

Instead of storing every frequency,

keep only

- Candidate
- Count

Initialize

```python
candidate = None
count = 0
```

Traverse the array.

If

```python
count == 0
```

Choose the current element as the new candidate.

If

```python
candidate == current_element
```

Increase count.

Otherwise,

decrease count.

---

# Pair Cancellation Concept

Every occurrence of a different element cancels one occurrence of the current candidate.

Example

```text
Candidate = 2

Array

2 2 1 1 2
```

Pair Cancellation

```text
2 ↔ 1

2 ↔ 1

Remaining

2
```

Since the majority element appears more than n/2 times,

it can never be completely cancelled.

Therefore,

it survives as the final candidate.

---

# Dry Run

Input

```python
arr = [2,2,1,1,1,2,2]
```

| Element | Candidate | Count |
|---------|-----------|-------|
|2|2|1|
|2|2|2|
|1|2|1|
|1|2|0|
|1|1|1|
|2|1|0|
|2|2|1|

Final Candidate

```text
2
```

---

# Verification Pass

LeetCode 169 guarantees that a majority element always exists.

Therefore,

the final candidate is the answer.

If the problem does NOT guarantee a majority element,

perform another traversal.

Count the frequency of the candidate.

Return it only if

```python
count > n//2
```

Otherwise,

return

```text
No Majority Element
```

---

# Complexity

Time

```text
O(n)
```

Space

```text
O(1)
```

---

# Comparison

| Approach | Time | Space |
|----------|------|--------|
| Brute Force | O(n²) | O(1) |
| HashMap | O(n) | O(n) |
| Moore's Voting | O(n) | O(1) |

---

# Advantages

- Single traversal
- Constant extra space
- Very efficient
- Easy to implement
- Frequently asked in coding interviews

---

# Common Mistakes

- Forgetting to reset the candidate when count becomes 0.
- Assuming the candidate is always correct when no majority is guaranteed.
- Using >= n/2 instead of > n/2.
- Forgetting the verification pass when required.

---

# Interview Tips

If the interviewer says

- Majority Element
- Appears more than half the time
- O(1) Extra Space
- Frequency greater than n/2

Immediately think

**Moore's Voting Algorithm**

---

# Pattern Recognition

Use Moore's Voting Algorithm when:

- Majority element exists.
- O(1) extra space is required.
- Frequency is greater than n/2.

---

# LeetCode Problems

## 169. Majority Element

Difficulty

Easy

Pattern

Moore's Voting Algorithm

Status

✅ Solved

---

## Bonus Reading

229. Majority Element II

Difficulty

Medium

Status

📖 Problem Read

---

# Questions Completed Today

## Local Practice

- Moore's Voting Algorithm
- Majority Element
- Dry Run Exercises
- Practice Questions
- Interview Questions

## LeetCode

- 169. Majority Element

---

# Key Takeaways

- Majority Element appears more than n/2 times.
- Moore's Voting Algorithm uses Candidate and Count.
- Pair Cancellation is the core idea.
- Verification pass is required only when a majority element is not guaranteed.
- The algorithm runs in O(n) Time and O(1) Space.

---

# Status

✅ Day 13 Completed