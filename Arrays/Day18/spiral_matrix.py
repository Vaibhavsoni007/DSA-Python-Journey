# -----------------------------------------
# 📘 spiral_print.py (Task 1)
# Print the matrix in spiral order
# -----------------------------------------

def spiral_print(matrix):
    result = []
    top, bottom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1

    while top <= bottom and left <= right:
        # Traverse from Left to Right
        for i in range(left, right + 1):
            result.append(matrix[top][i])
        top += 1

        # Traverse from Top to Bottom
        for i in range(top, bottom + 1):
            result.append(matrix[i][right])
        right -= 1

        # Traverse from Right to Left
        if top <= bottom:
            for i in range(right, left - 1, -1):
                result.append(matrix[bottom][i])
            bottom -= 1

        # Traverse from Bottom to Top
        if left <= right:
            for i in range(bottom, top - 1, -1):
                result.append(matrix[i][left])
            left += 1

    # Print result in spiral order
    print(" ".join(map(str, result)))


# -----------------------------------------
# 📘 spiral_matrix.py (Task 2)
# Return the spiral traversal as a list
# -----------------------------------------

def spiral_matrix(matrix):
    result = []
    top, bottom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1

    while top <= bottom and left <= right:
        # Traverse from Left to Right
        for i in range(left, right + 1):
            result.append(matrix[top][i])
        top += 1

        # Traverse from Top to Bottom
        for i in range(top, bottom + 1):
            result.append(matrix[i][right])
        right -= 1

        # Traverse from Right to Left
        if top <= bottom:
            for i in range(right, left - 1, -1):
                result.append(matrix[bottom][i])
            bottom -= 1

        # Traverse from Bottom to Top
        if left <= right:
            for i in range(bottom, top - 1, -1):
                result.append(matrix[i][left])
            left += 1

    return result


# -----------------------------------------
# 🚀 Example Usage
# -----------------------------------------
if __name__ == "__main__":
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    print("Task 1 Output (Print):")
    spiral_print(matrix)   # Expected: 1 2 3 6 9 8 7 4 5

    print("\nTask 2 Output (List):")
    print(spiral_matrix(matrix))  # Expected: [1,2,3,6,9,8,7,4,5]
