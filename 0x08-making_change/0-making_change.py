#!/usr/bin/python3
'''
Make Change
'''


def makeChange(coins, total):
    """
    Make Change Function

    Args:
        coins: List of coins
        total: number (int)
    """
    if total <= 0:
        return 0

    coins.sort(reverse=True)

    coin_count = 0
    remaining = total

    for coin in coins:
        if remaining <= 0:
            break

        num_coins = remaining // coin
        coin_count += num_coins
        remaining -= num_coins * coin

    if remaining > 0:
        return -1

    return coin_count
