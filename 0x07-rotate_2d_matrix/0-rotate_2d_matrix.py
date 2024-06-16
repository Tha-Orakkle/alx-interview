#!/usr/bin/python3
"""
Rotate 2D Matrix
"""

# APPROACH
# 1. transpose the matrix
# 2. then reverse the list
# time complexity: O(N^2) + O(N^2)
# space complexity: O(1)


def rotate_2d_matrix(matrix):
    """rotates a n x n 2D matrix 90 degrees clockwise"""

    # Transpose 2D Matrix
    for i in range(len(matrix)):
        for j in range(i, len(matrix)):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reverse a 2D Matrix
    for i in range(len(matrix)):
        matrix[i].reverse()

    return matrix
