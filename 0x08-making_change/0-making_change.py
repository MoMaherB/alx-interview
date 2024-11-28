#!/usr/bin/python3
"""
Determine the fewest number of coins needed
to meet a given amount.
"""


def makeChange(coins, total):
    """
    Main file for testing
    """
    if total <= 0:
        return 0
    if not coins:
        return -1

    coins.sort(reverse=True)
    fewest_number = 0
    for coin in coins:
        if total < coin:
            continue
        fewest_number += total // coin
        total %= coin
        if total == 0:
            break
    if total != 0:
        return -1
    return fewest_number
