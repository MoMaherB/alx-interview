#!/usr/bin/python3
"""lockboxes"""


def canUnlockAll(boxes):
	"""
    lockboxes method
    """
	unlocked =[True]

	for i in range(1, len(boxes)):
		unlocked.insert(i, False)


	for i, box in enumerate(boxes):
		if not unlocked[i]:
			print(f"Unlocked boxes: {unlocked}")
			return False
		
		for key in box:
			if key in range(len(boxes)):
				unlocked[key] = True
				for internal_box in boxes[key]:
					unlocked[internal_box] = True
	return True


