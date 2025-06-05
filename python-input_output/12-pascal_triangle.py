#!/usr/bin/python3
"""This module provides a function to generate a pascal triangle."""
def pascal_triangle(n):
    """
    Generate Pascal's triangle of size n.
    
    Args:
        n: The number of rows in Pascal's triangle.

    return: a list of lists representing Pascal's triangle of size n."""
    if n <= 0:
        return []
    pascal = [[1]]

    for i in range(1, n):
        last = pascal[-1]
        current = [1]

        for j in range(1, len(last)):
            current.append(last[j-1] + last[j])

        current.append(1)
        pascal.append(current)

    return pascal
