#!/usr/bin/env python3

COIN_AMOUNTS = [1, 2, 5, 10, 20, 50, 100, 200]

def split_sum(amount, coins):
    if amount == 0:
        return 1
    if amount < 0 or not coins:
        return 0
    return split_sum(amount - coins[0], coins) + split_sum(amount, coins[1:])

if __name__ == '__main__':
    print(split_sum(200, COIN_AMOUNTS))