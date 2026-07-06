# 🇳🇱 Dutch National Flag Algorithm: Interview Deep-Dive

This document covers the core theory, invariants, mechanics, and interview applications of the Dutch National Flag (DNF) algorithm (Three-Way Partitioning).

---

## 💡 Conceptual Overview

### 1. The Origin
The algorithm was designed by the famous computer scientist **Edsger Dijkstra**. He named it after the national flag of his home country, the Netherlands. The flag consists of three horizontal stripes: **Red, White, and Blue**. 

Dijkstra framed the problem of sorting an array of scattered red, white, and blue elements into their proper flag order using minimal memory and time. In coding terms, this translates directly to sorting an array of `0`s (Red), `1`s (White), and `2`s (Blue) in a single pass.

---

## 🎯 The Loop Invariant (How it Works)

### 2. Why Three Pointers Instead of Two?
Two pointers can only manage a binary split between two distinct categories (e.g., separating Evens vs. Odds, or Zeroes vs. Non-Zeroes). 

Because we need to sort **three** categories, we must maintain **four distinct zones** in the array simultaneously. This requires three boundaries managed by three pointers: `low`, `mid`, and `high`.

### 3. State of the Array During Execution
At any point during the loop, the algorithm strictly maintains the following zones:

| Array Index Range | Logical Zone | Meaning / Contents |
| :--- | :--- | :--- |
| `0` to `low - 1` | **Red Zone** | All elements are strictly `0` |
| `low` to `mid - 1` | **White Zone** | All elements are strictly `1` |
| `mid` to `high` | **Unknown Zone** | Elements that have **not** been processed yet |
| `high + 1` to `End` | **Blue Zone** | All elements are strictly `2` |

---

## 🔍 Critical Mechanics & Edge Cases

### 4. Why is `mid` NOT incremented after swapping with `high`?

When `arr[mid] == 2`, we swap it with `arr[high]` and decrement `high`. 

> ⚠️ **The Core Reason:** The element currently sitting at `high` comes from the **Unknown Zone**. We have absolutely no idea what value it holds—it could be a `0`, a `1`, or another `2`. 

* If we blindly incremented `mid` after the swap, we would leave that new, unexamined element behind us.
* If that swapped element happened to be a `0` or a `2`, it would end up trapped in the middle of the `1`s (the White Zone), breaking our loop invariant.
* Therefore, we keep `mid` exactly where it is so the very next iteration can evaluate the freshly swapped element.

*Note: Conversely, when swapping `arr[mid] == 0` with `arr[low]`, we safely increment both `low` and `mid` because we know the element coming from `low` is guaranteed to be a `1`.*

---

## 🚀 Generalization & Interview Applications

### 5. Can this algorithm work for numbers other than 0, 1, and 2?
**Yes.** The algorithm is fundamentally a **Three-Way Partitioning** strategy. It does not care about the literal integers `0`, `1`, and `2`. It only cares that data can be mapped into three ordered buckets:

* **Bucket 1 (Low):** Belongs at the beginning.
* **Bucket 2 (Mid):** Belongs in the middle.
* **Bucket 3 (High):** Belongs at the end.

*Example:* You can use this exact logic to sort characters `['C', 'A', 'B']` into `['A', 'A', 'B', 'B', 'C', 'C']` by redefining your conditional checks for `'A'` and `'C'`.

### 6. Famous Interview Problems Based on This Idea

* **LeetCode 75 - Sort Colors:** The direct literal application of this algorithm.
* **3-Way Quicksort (Dual-Pivot Quicksort):** Standard Quicksort degrades to $O(n^2)$ time complexity when an array contains many duplicate keys. By using the DNF multi-pointer approach as the partition step, you can group all duplicate pivot elements into the center zone simultaneously, keeping Quicksort highly efficient at $O(n \log n)$.
* **Three-Way Array Partitioning:** Variations where you partition an array around a range $[a, b]$, such that all elements smaller than $a$ come first, elements between $a$ and $b$ come next, and elements greater than $b$ come last.
* **Move Elements / Sign Segregation:** Problems asking you to organize an array such that all negative numbers are on the left, zeroes are in the middle, and positive numbers are on the right in a single pass.