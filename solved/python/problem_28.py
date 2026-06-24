#!/usr/bin/env python3

# Starting with the number and moving to the right in a clockwise direction a by

# spiral is formed as follows:

# 21 22 23 24 25
# 20  7  8  9 10
# 19  6  1  2 11
# 18  5  4  3 12
# 17 16 15 14 13

# It can be verified that the sum of the numbers on the diagonals is 101.

# What is the sum of the numbers on the diagonals in a
# 1001 by 10001 spiral formed in the same way?


def sum_spiral_diagonals(size: int = 1001) -> int:
    total = 1
    current_number = 1

    for layer in range(1, (size // 2) + 1):
        for corner in range(4):
            current_number += layer * 2
            total += current_number

    return total

if __name__ == '__main__':
    print(sum_spiral_diagonals())
