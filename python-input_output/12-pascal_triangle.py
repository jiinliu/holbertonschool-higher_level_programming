#!/usr/bin/python3
def pascal_triangle(n):
    """Returns a list of lists representing Pascal's triangle of size n."""
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
