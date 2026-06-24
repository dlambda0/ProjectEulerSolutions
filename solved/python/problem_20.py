#!/usr/bin/env python3

from math import factorial
from functools import reduce


def digit_sum(num):
    return reduce(lambda x, y: x + y, [int(char) for char in str(num)])


if __name__ == '__main__':
    num = factorial(100)
    answer = digit_sum(num)
    print(f'ANSWER: {answer}')