#!/usr/bin/python3
"""
This is module contain a function that divides all elements of a matrix
"""


def matrix_divided(matrix, div):
    """
    This function divide all elements of a matrix

    Args:
        matrix: A matrix
        div: the number to divide each element
    Return:
        new matrix
    """
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats"
                )
        for col in row:
            if not isinstance(col, int) or isinstance(col, float):
                raise TypeError(
                    "matrix must be a matrix\
 (list of lists) of integers/floats"
                    )

    if div == 0:
        raise ZeroDivisionError("division by zero")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    new_matrix = [[round(col/div, 2) for col in row] for row in matrix]
    return new_matrix
