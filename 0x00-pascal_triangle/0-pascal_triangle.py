#!/usr/bin/python3
"""
function that creates a pascal triangle
"""


def pascal_triangle(n):
    """creates the pascal triangle"""
    triangle = []
    if n <= 0:
        return triangle
    for _ in range(n):
        row = [1]
        if triangle:
            last_row = triangle[-1]
            row.extend(sum(pair) for pair in zip(last_row[1:], last_row))
            row.append(1)
        triangle.append(row)
    return triangle
