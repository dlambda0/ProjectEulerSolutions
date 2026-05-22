#!/usr/bin/env python3

import math

# stolen form geeksforgeeks
def sum_of_divisors(n):
    if n <= 1:
        return 0
    s = 1
    p = 2
    while p * p <= n:
        if n % p == 0:
            s += p
            q = n // p
            if q != p:
                s += q
        p += 1
    return s


def evaluate():
    acc = 0
    abundants = [i for i in range(12, 28123) if sum_of_divisors(i)]
    
    for i, a in enumerate(abundants):
        
    return acc

if __name__ == '__main__':
    print(evaluate())