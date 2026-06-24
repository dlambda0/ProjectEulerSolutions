#!/usr/bin/env python3

# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17

# Find the sum of all the primes below two million.

from functools import reduce
from sympy import isprime  # lost my previous is_prime so I am using sympy


def primes_below(max=2000000) -> list[int]:
    return [num for num in range(max) if isprime(num)]


if __name__ == "__main__":
    print(
        reduce(
            lambda x, y: x + y,
            primes_below(),
        )
    )
