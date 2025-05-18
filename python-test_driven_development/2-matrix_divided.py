#!/usr/bin/python3
"""
Provides a function to divide all elements of a matrix by a number.

"""

def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by div, rounded to 2 decimal places.

    Args:
        matrix (list of lists of int/float): The matrix to divide.
        div (int or float): The number to divide by.

    Returns:
        list of lists of float: New matrix with divided elements.

    Raises:
        TypeError: If matrix is not a list of lists of numbers,
                   or if div is not a number.
        TypeError: If rows of the matrix are not the same size.
        ZeroDivisionError: If div is zero.
    """
    if (not isinstance(matrix, list) or
        not all(isinstance(row, list) for row in matrix) or
        not all(isinstance(item, (int, float)) for row in matrix for item in row)):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if len(matrix) > 0 and any(len(row) != len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(item / div, 2) for item in row] for row in matrix]
