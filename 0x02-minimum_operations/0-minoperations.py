#!/usr/bin/env python3
"""minimum operations"""


def minOperations(n: int) -> int:
    """calculates the fewest number of operations
    needed to result in exactly n H"""
    if n <= 1:
        return 0

    inp = "H"
    mul = 1
    result = "H"
    moves = 0
    while len(result) < n:
        if n % len(result) == 0:
            mul = len(result)
            moves += 1
        result += inp * mul
        moves += 1
    return moves
