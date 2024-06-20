#!/usr/bin/python3

def makeChange(coins, total):
    """
    Calculate the fewest no of coins to make up a certain amount of money.
    """
    dp = [total + 1] * (total + 1)
    dp[0] = 0

    for t in range(1, total + 1):
        for c in coins:
            if t - c >= 0:
                dp[t] = min(dp[t], 1 + dp[t - c])

    return dp[total] if dp[total] != total + 1 else -1
