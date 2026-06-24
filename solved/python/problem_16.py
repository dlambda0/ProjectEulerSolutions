#!/usr/bin/env python3

# 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26

# what is the sum of the digits of number 2^1000

from functools import reduce


def list_reformat(num_list) -> list[int]:
    return [int(num) for num in num_list]


if __name__ == "__main__":
    num_list = list(str(2**1000))
    print(reduce(lambda x, y: x + y, list_reformat(num_list)))
