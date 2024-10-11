#!/usr/bin/python3
"""lockboxes"""


def canUnlockAll(boxes):
    """
    lockboxes method
    """
    unlocked = [True]

    for i in range(1, len(boxes)):
        unlocked.insert(i, False)

    for i, box in enumerate(boxes):
        if not unlocked[i]:
            continue

        for key in box:
            if key in range(len(boxes)):
                unlocked[key] = True
                for internal_box in boxes[key]:
                    if internal_box in range(len(unlocked)):
                        unlocked[internal_box] = True
            if all(unlocked):
                break

    return True
