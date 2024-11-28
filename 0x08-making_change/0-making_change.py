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

    coins.sort(reverse=True)
    fewest_number = 0
    for coin in coins:
        if total < coin:
            return -1
        fewest_number += int(total / coin)
        total %= coin
        if total == 0:
            break
    return fewest_number
