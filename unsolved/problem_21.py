#!/usr/bin/env python3

# I did it somewhat functionally!


def find_divisors(num) -> list[int]:
    return [x for x in range(1, (num // 2) + 1) if num % x == 0] 


def divisors_sum(num) -> int:
    return sum(find_divisors(num))


def is_amicable(first) -> bool:
    second = divisors_sum(first)
    return second != first and divisors_sum(second) == first


def amicable_nums(max) -> list[int]:
    return [x for x in range(1, max) if is_amicable(x)]


if __name__ == "__main__":
    print(sum(amicable_nums(10000)))
