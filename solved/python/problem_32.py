#!/usr/bin/env python3

from functools import reduce
from itertools import permutations


def numberize(snums):
    return int(reduce(lambda x, y: x + y, snums))


def is_pandigital_product(snums):
    return numberize(snums[0:2]) * numberize(snums[2:5]) == numberize(
        snums[5:9]
    ) or numberize(snums[0:1]) * numberize(snums[1:5]) == numberize(snums[5:9])


def eval(data):
    ans = []

    for snums in data:
        if is_pandigital_product(snums) and not (numberize(snums[5:9]) in ans):
            ans.append(numberize(snums[5:9]))

    return sum(ans)


if __name__ == "__main__":
    data = list(permutations("123456789"))
    print(eval(data))
