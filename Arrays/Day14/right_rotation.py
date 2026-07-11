"""

Implement right rotation using an extra array.

Input

arr = [1,2,3,4,5]
k = 2

Output

[4,5,1,2,3]

"""

class Solution:
    def rotate(self, arr: list[int], k: int) -> list[int]:
        n = len(arr)
        k = k % n
        temp = [0] * n
        for i in range(n):
            temp[(i + k) % n] = arr[i]
        return temp


if __name__ == "__main__":
    sol = Solution()
    arr = [1, 2, 3, 4, 5]
    k = 2
    print(sol.rotate(arr, k))