#!/usr/bin/python3
"""Unlocks boxes"""


def canUnlockAll(boxes):
    """checks if all boxes can be unlocked"""
    if not boxes or not boxes[0]:
        return False
    opened_boxes = set([0])
    keys_available = boxes[0]

    while keys_available:
        current_key = keys_available.pop()

        if 0 <= current_key < len(boxes) and current_key not in opened_boxes:
            opened_boxes.add(current_key)
            keys_available.extend(boxes[current_key])

    return len(opened_boxes) == len(boxes)
