#!/usr/bin/python3
"""
This module contains the function rotate_2d_matrix
which rotates a matrix 90 degrees clockwise.
"""


def rotate_2d_matrix(matrix):
    """
    Rotates a 2D matrix 90 degrees clockwise in place.
    Args:
        matrix: The n x n matrix to be rotated.
    """
    n = len(matrix)
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for i in range(n):
        matrix[i].reverse()
