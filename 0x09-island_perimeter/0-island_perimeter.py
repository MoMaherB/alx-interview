#!/usr/bin/python3
"""
0-island_perimeter.py
"""


def island_perimeter(grid):
    """
    Calculate the perimeter of an island described in the grid.
    """
    rows = len(grid)
    cols = len(grid[0])
    left = 0
    top = 0
    right = 0
    bottom = 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                if i == 0 or grid[i - 1][j] == 0:
                    top += 1
                if i == rows - 1 or grid[i + 1][j] == 0:
                    bottom += 1
                if j == 0 or grid[i][j - 1] == 0:
                    left += 1
                if j == cols - 1 or grid[i][j + 1] == 0:
                    right += 1

    return top + bottom + left + right
