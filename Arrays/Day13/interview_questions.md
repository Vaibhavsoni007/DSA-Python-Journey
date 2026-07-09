### Step-by-Step Breakdown of the Logic
* **`count == 0`**: Represents a clean slate. Since previous pairings have completely canceled each other out, we establish the current element as a new potential `candidate` and set its "survival count" to 1.
* **`num == candidate`**: The current element is an ally. We increment the `count` because this strengthens the candidate's position.
* **`num != candidate`**: The current element is an opponent. A battle occurs! One instance of the candidate and this opponent cancel each other out (`count -= 1`).

Because the true majority element has a structural advantage (holding $> 50\\%$ of the total population), it can never be completely permanently erased by the minority.

---

## 🔍 Interview Question 2: When should we perform a second pass after Moore's Voting Algorithm?

### The Short Answer
You **must** perform a second pass whenever the problem constraints do not explicitly guarantee that a majority element *always* exists in the input array.

### Why the First Pass is Not Enough
The first pass of Moore's Voting Algorithm is a **candidate-finding mechanism**, not a verification mechanism. It operates under a conditional guarantee: *If a majority element exists, this algorithm will find it.* 

However, if a majority element does **not** exist, the first pass will still output a candidate—which will be completely incorrect.

### Scenario Comparison

#### 1. When a Majority Element EXISTS (`[3, 2, 3]`)
* **Pass 1:** Cancels opposing pairs. Candidate `3` survives.
* **Result:** `3` is the correct majority element.

#### 2. When NO Majority Element Exists (`[1, 2, 3]`)
* **Pass 1:** 
  * `1` becomes candidate (`count = 1`).
  * `2` cancels `1` (`count = 0`).
  * `3` becomes candidate (`count = 1`).
* **Result:** The algorithm outputs `3` as the candidate. However, `3` only appears $1$ time, which is NOT $> \\\\lfloor 3/2 \\\\rfloor$. The answer should be "No majority element".

### How to Implement the Second Pass
To prevent false positives, you loop through the array a second time strictly to **count the actual occurrences** of the selected candidate.

```python
# --- Pass 1: Find Candidate ---
candidate = find_candidate(arr)

# --- Pass 2: Verify Candidate (The Second Pass) ---
actual_count = 0
for num in arr:
    if num == candidate:
        actual_count += 1

# Check against the strict majority threshold (> n // 2)
if actual_count > len(arr) // 2:
    return candidate
else:
    return -1  # Or None, indicating no majority element exists