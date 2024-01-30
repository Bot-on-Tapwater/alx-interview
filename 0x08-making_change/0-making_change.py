#!/usr/bin/python3
"""Implement makeChange() function"""


def makeChange(coins, total):
    """
    Calculates the minimum number of coins
    needed to make change for a given total amount.

    Args:
        coins (List[int]): The denominations of the available coins.
        total (int): The total amount for which to make change.

    Returns:
        int: The minimum number of coins needed to make change for the total
        amount. Returns -1 if it's not possible to make change.
    """

    if total <= 0:
        return 0

    """
    Initialize an array to store the minimum
    number of coins needed for each amount
    """
    dp = [float('inf')] * (total + 1)

    # There are 0 coins needed to make change for amount 0
    dp[0] = 0

    '''
    Iterate through each coin and update the
    minimum number of coins for each amount
    '''
    for coin in coins:
        for amount in range(coin, total + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    """
    If the value at the total amount is still infinity,
    it means it's not possible to make change
    """
    return dp[total] if dp[total] != float('inf') else -1
