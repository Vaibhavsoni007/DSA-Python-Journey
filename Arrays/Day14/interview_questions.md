# Interview Study Notes: Array Rotation

## 📌 Interview Question 1: Why do we write `k = k % len(arr)`?

### 🔹 Explanation
The operation `k = k % len(arr)` uses the modulo operator (`%`) to calculate the remainder of dividing $k$ by the length of the array ($n$). 

When you rotate an array of length $n$ exactly $n$ times, every element shifts all the way around and lands exactly back in its starting position. Therefore, rotating an array of size $n$ by $n, 2n, 3n$ steps changes absolutely nothing. 

Because of this cyclic behavior, rotating an array by any large number $k$ produces the exact same layout as rotating it by just the remainder: $k \% n$.

Writing this line serves two vital purposes:
1. **Performance Optimization:** It eliminates completely redundant, full-circle shifts.
2. **Safety Check:** It protects your code from `IndexOutOfBounds` exceptions by constraining $k$ to a valid index range $[0, n-1]$.

### 🔹 Practical Example
Let's trace an array `arr = [10, 20, 30]` where length $n = 3$, and we want to left-rotate it by $k = 8$ steps.

* **1st shift:** `[20, 30, 10]`
* **2nd shift:** `[30, 10, 20]`
* **3rd shift:** `[10, 20, 30]` *(Full circle! Back to start)*
* **4th shift:** `[20, 30, 10]`
* **5th shift:** `[30, 10, 20]`
* **6th shift:** `[10, 20, 30]` *(Full circle again!)*
* **7th shift:** `[20, 30, 10]`
* **8th shift:** `[30, 10, 20]`

Instead of spinning in circles 8 times, we apply the formula:
$$k = 8 \% 3 = 2$$

Rotating the array just **2 times** gets us to `[30, 10, 20]` instantly, skipping 6 completely useless operations.

---

## 📌 Interview Question 2: Approach Comparison

### 🔹 Efficiency Table

| Approach | Time Complexity | Space Complexity |
| :--- | :--- | :--- |
| **Brute Force** | $O(n \times k)$ | $O(1)$ |
| **Extra Array** | $O(n)$ | $O(n)$ |
| **Reversal Algorithm** | $O(n)$ | $O(1)$ |

### 🔹 Which approach is preferred in interviews?
The **Reversal Algorithm** is the golden standard and the expected answer in a technical interview.

### 🔹 Why?
Interviewers use array rotation to see if you can optimize time and space complexities simultaneously without trading one for the other.

* **Why Brute Force fails:** Shifting elements one-by-one $k$ times is incredibly inefficient. If $k$ is roughly equal to $n$, the time complexity degrades to $O(n^2)$. For an array with 100,000 items, this approach would lock up the system.
* **Why Extra Array is rejected:** While it runs fast at $O(n)$ time, creating a backup array of size $n$ requires allocating duplicate memory. If you are operating on memory-restricted hardware or processing massive real-world datasets, duplicating an array is a massive waste of resources.
* **Why Reversal wins:** It delivers optimal linear time $O(n)$ while maintaining a constant space footprint of $O(1)$. It proves to the interviewer that you know how to leverage array symmetries and manipulate direct memory pointers efficiently.

---

## 📌 Interview Question 3: Why is the Reversal Algorithm considered an "In-Place" algorithm?

### 🔹 Explanation
An algorithm is formally classified as **in-place** if it updates the input data structure directly within its original memory slots, rather than copying or creating a new data structure to hold the output. Its auxiliary (extra) space requirement must be constant, denoted as $O(1)$.

The Reversal Algorithm is strictly in-place due to three structural facts:
1. **Direct Mutation:** The element swapping happens directly inside the original array container (`arr[start], arr[end] = arr[end], arr[start]`).
2. **No Data Scaling:** It does not allocate new arrays, lists, or dynamic structures that grow when the input grows.
3. **Fixed Memory Footprint:** The only extra variables declared are simple integer pointers (`start`, `end`, `k`, `n`). These take up a microscopic, fixed amount of bytes whether you are rotating an array of 5 integers or 5,000,000 integers.

### 🔹 Visual Breakdown
Watch how the pointers modify the data structure directly without generating any secondary arrays:

```text
Initial Array: [1, 2, 3, 4, 5]
                ^           ^
              start        end    --> Swap elements directly in-place

Step 1 Result: [5, 2, 3, 4, 1]
                   ^     ^
                 start  end    --> Move pointers inward and swap again

Final Result:  [5, 4, 3, 2, 1]