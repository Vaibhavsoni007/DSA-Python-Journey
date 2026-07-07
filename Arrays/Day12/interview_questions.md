# Interview Questions on Kadane's Algorithm

---

## Question 1: Why do we reset `current_sum = 0` when it becomes negative?

### Explanation
Kadane's Algorithm is used to find the **maximum sum subarray**.  
If the running sum (`current_sum`) becomes negative, it will only reduce the sum of any future subarray we try to build.  
Therefore, instead of carrying forward a negative sum, we reset it to `0` and start fresh from the next element.

This ensures that we only consider subarrays that have the potential to increase the overall maximum sum.

### Example
Consider the array:

arr = [4, -5, 6, -2, 3]


Step-by-step:
- Start with `current_sum = 0`
- Add `4` → `current_sum = 4` → max_sum = 4
- Add `-5` → `current_sum = -1` (negative, so reset to 0)
- Add `6` → `current_sum = 6` → max_sum = 6
- Add `-2` → `current_sum = 4`
- Add `3` → `current_sum = 7` → max_sum = 7

Final answer: **Maximum sum subarray = 7** (from `[6, -2, 3]`)

👉 Resetting avoided carrying the `-1` forward, which would have reduced the sum.

---

## Question 2: Can Kadane's Algorithm work if we need the **minimum sum subarray**?

### Explanation
Yes, Kadane’s Algorithm can be adapted to find the **minimum sum subarray**.  
The logic is similar, but instead of resetting when the sum becomes negative, we reset when the sum becomes **positive**.  

Why?  
- For maximum sum, negative values hurt the sum, so we discard them.  
- For minimum sum, positive values increase the sum, so we discard them.

### Modified Logic
- Track `current_sum` for minimum.  
- If `current_sum > 0`, reset it to `0`.  
- Keep updating `min_sum` with the smallest value seen.

### Example
Consider the array:

arr = [3, -4, 2, -3, -1, 7, -5]


Step-by-step:
- Start with `current_sum = 0`
- Add `3` → `current_sum = 3` → reset to 0 (since positive)
- Add `-4` → `current_sum = -4` → min_sum = -4
- Add `2` → `current_sum = -2`
- Add `-3` → `current_sum = -5` → min_sum = -5
- Add `-1` → `current_sum = -6` → min_sum = -6
- Add `7` → `current_sum = 1` → reset to 0
- Add `-5` → `current_sum = -5`

Final answer: **Minimum sum subarray = -6** (from `[-4, 2, -3, -1]`)

---

## Key Takeaways
- **[Kadane’s Algorithm](ca://s?q=Explain_Kadane's_Algorithm)** resets `current_sum` when it becomes negative to avoid reducing future sums.  
- For **[minimum sum subarray](ca://s?q=Kadane's_for_minimum_sum_subarray)**, the reset condition flips: we reset when `current_sum` becomes positive.  
- Both problems use the same principle: discard sums that cannot contribute positively to the desired result.
