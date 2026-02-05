#!/usr/bin/env python3

from functools import reduce


def split_square_sum(num: int):
    return sum(int(digit) ** 2 for digit in str(num))


def test_for_89(max: int):
    eighty_nine_sum = 0

    for i in range(1, max):
        chain_num = i
        print(chain_num)
        while chain_num != 1 and chain_num != 89:
            chain_num = split_square_sum(chain_num)
        if chain_num == 89:
            eighty_nine_sum += 1

    return eighty_nine_sum


if __name__ == "__main__":
    MAX_NUM = 10000000
    print(test_for_89(MAX_NUM))
