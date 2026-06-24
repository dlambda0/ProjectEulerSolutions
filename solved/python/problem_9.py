#!/usr/bin/env python3

from math import prod


def is_pythagorean_triplet(a, b, c) -> bool:
    return (a < b < c) and (a**2 + b**2 == c**2)


def find_pythagorean_triplet(num=1000) -> tuple[int, int, int]:
    for a in range(1, num // 3):
        for b in range(a + 1, (num - a) // 2):
            c = num - a - b
            if is_pythagorean_triplet(a, b, c):
                return a, b, c
    return None


if __name__ == "__main__":
    triplet = find_pythagorean_triplet()
    product = prod(triplet)
    print(f"The triplet is {triplet}")
    print(f"The product is {product}")
