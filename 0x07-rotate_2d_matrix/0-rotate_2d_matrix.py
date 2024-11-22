#!/usr/bin/python3
"""
Given an n x n 2D matrix, rotate it 90 degrees clockwise.
"""


def rotate_2d_matrix(matrix):
    """
    Test 0x07 - Rotate 2D Matrix
    """

    array_lenth = len(matrix)
    if not array_lenth or array_lenth != len(matrix[0]):
        return

    for i in range(array_lenth):
        for j in range(int(array_lenth / 2) + i):
            if i == j:
                continue
            temp = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = temp

    for i in range(array_lenth):
        for j in range(int(array_lenth/2)):
            temp = matrix[i][j]
            matrix[i][j] = matrix[i][array_lenth - j - 1]
            matrix[i][array_lenth - j - 1] = temp
