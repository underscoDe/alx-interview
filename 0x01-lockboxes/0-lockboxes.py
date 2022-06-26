#!/usr/bin/python3
"""Solution to Lockboxes problem"""


def canUnlockAll(boxes):
    """Determines if all the boxes can be opened"""
    if (type(boxes) is not list or len(boxes) == 0):
        return False
    unlocked = [0]
    for key in unlocked:
        for val in boxes[key]:
            if val not in unlocked:
                unlocked.append(val)
    if len(unlocked) == len(boxes):
        return True
    return False
