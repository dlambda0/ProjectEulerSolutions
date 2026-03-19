#!/usr/bin/env python3

from typing import List


def divisor_sum(num: int) -> int:
    return sum([x for x in range(1, (num // 2) + 1) if num % x == 0])


def is_nonabundant_sum(num: int, abundant_nums) -> bool:
    abundant_nums = [x for x in abundant_nums if x <= num]
    for x in abundant_nums:
        if (num - x) in abundant_nums:
            return True

    print(num)
    return False


def non_abundant_sums() -> int:
    abundant_nums: List[int] = [x for x in range(1, 28124) if divisor_sum(x) > x]
    return sum([x for x in range(1, 28124) if is_nonabundant_sum(x, abundant_nums)])


if __name__ == "__main__":
    print(non_abundant_sums())
