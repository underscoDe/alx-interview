#!/usr/bin/python3
"""Solution to Lockboxes problem"""


def canUnlockAll(boxes):
    """Determines if all the boxes can be opened"""
    if (type(boxes) is not list):
        return False
    unlocked = [0]
    for key in unlocked:
        for v in boxes[key]:
            if v not in unlocked:
                unlocked.append(v)
    return len(unlocked) == len(boxes)
