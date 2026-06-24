#!/usr/bin/env python3

import math

def digit_factorial(n):
    return sum(math.factorial(int(digit)) for digit in str(n))

if __name__ == '__main__':
    ans = 0
    for n in range(3, 999999):
        out = digit_factorial(n)
        if out == n:
            ans += out
            
    print(ans)

