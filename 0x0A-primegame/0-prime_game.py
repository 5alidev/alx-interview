#!/usr/bin/python3
"""
Module to find a winner in a Prime Game
"""


def sieve_of_eratosthenes(max_n):
    """
    Returns a list where primes[i] is True if i is prime,
    False otherwise.
    """

    primes = [True] * (max_n + 1)
    primes[0] = primes[1] = False
    for i in range(2, int(max_n ** 0.5) + 1):
        if primes[i]:
            for multiple in range(i * i, max_n + 1, i):
                primes[multiple] = False
    return primes


def isWinner(x, nums):
    if x < 1 or not nums:
        return None

    max_n = max(nums)
    primes = sieve_of_eratosthenes(max_n)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        primes_in_game = sum(primes[2:n+1])
        if primes_in_game % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
