#!/usr/bin/python3
"""This module contains function pascal triangle"""


def pascal_triangle(n):
    """
    This function returns a list of lists of integers
    representing the Pascal’s triangle of n
    """
    triangle = []
    if n < 1:
        return triangle
    for index in range(n):
        row = []
        if index == 0:
            row.append(1)
        else:
            prev_row = triangle[index - 1]
            for row_index in range(index + 1):
                if row_index == 0 or row_index == len(prev_row):
                    row.append(1)
                else:
                    print(
                        f"{prev_row[row_index - 1]} + {prev_row[row_index]} ")
                    row.append(prev_row[row_index - 1] + prev_row[row_index])
        triangle.append(row)
    return triangle
