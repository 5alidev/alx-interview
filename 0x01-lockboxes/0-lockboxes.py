#!/usr/bin/python3
"""
Lockboxes
"""


def canUnlockAll(boxes):
    """
    Check if you can unlock all boxes.
    :param boxes: List of lists of keys.
    :return: True if all boxes can be unlocked, False otherwise.
    """
    n = len(boxes)
    unlocked_boxes = set([0])
    queue = [0]

    while queue:
        current_box = queue.pop(0)
        for key in boxes[current_box]:
            if key < n and key not in unlocked_boxes:
                unlocked_boxes.add(key)
                queue.append(key)

    return len(unlocked_boxes) == n
