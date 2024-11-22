#!/usr/bin/python3
"""
Test 0x07 - Rotate 2D Matrix
"""
rotate_2d_matrix = __import__('0-rotate_2d_matrix').rotate_2d_matrix

if __name__ == "__main__":
    matrix = [[1, 2, 3, 44],
              [4, 5, 6, 77],
              [7, 8, 9, 88],
              [10, 11, 12, 13]]

    rotate_2d_matrix(matrix)
    print(matrix)
