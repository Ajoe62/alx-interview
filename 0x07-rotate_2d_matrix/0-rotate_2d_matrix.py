#!/usr/bin/python3

"""
This script rotates a given n x n 2D matrix 90 degrees clockwise in-place.
"""


def rotate_2d_matrix(matrix):
    """
    Rotate a given n x n 2D matrix 90 degrees clockwise in-place.

    Parameters:
    matrix (list[list[int]]): A 2D list representing the matrix to be rotated.

    Returns:
    None
    """
    # Transpose the matrix
    for i in range(len(matrix)):
        for j in range(i, len(matrix)):
            matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]
    # Reverse each row
    for i in range(len(matrix)):
        matrix[i] = matrix[i][::-1]
