#!/usr/bin/env python3

import math

# somewhat stolen lol

if __name__ == '__main__':
    numer = 1
    denom = 1
    for d in range(10, 100):
        for n in range(10, d):
            n0 = n % 10
            n1 = n // 10
            d0 = d % 10
            d1 = d // 10
            if (n1 == d0 and n0 * d == n * d1) or (n0 == d1 and n1 * d == n * d0):
                numer *= n
                denom *= d
    print(denom // math.gcd(numer, denom))
