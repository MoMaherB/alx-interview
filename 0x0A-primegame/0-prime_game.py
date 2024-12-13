#!/usr/bin/python3
"""
Maria and Ben are playing a game.
"""


def is_prime(number):
    """
    is_prime helper function
    """

    from math import sqrt, ceil
    if number <= 1:
        return False
    if number == 2:
        return True
    x = ceil(sqrt(number))
    for i in range(2, x + 1):
        if number % i == 0:
            return False
    return True


def isWinner(x, nums):
    """
    Maria and Ben are playing a game. Given a set of consecutive
    integers starting from 1 up to and including n
    """
    if x <= 0:
        return
    Maria = 0
    Ben = 0
    for round in nums:
        count_primes = 0
        for number in range(round + 1):
            if is_prime(number):
                count_primes += 1

        if count_primes % 2 == 0:
            Ben += 1
        else:
            Maria += 1
    if Ben > Maria:
        return "Ben"
    elif Ben == Maria:
        return
    else:
        return "Maria"
