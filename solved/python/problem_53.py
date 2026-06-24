#!/usr/bin/env python3

from math import factorial

def comb(n, r):
    return factorial(n) / (factorial(r) * factorial(n - r))

def evaluate():
    total = 0
    
    for i in range(23, 101):
        for j in range(i):
            if comb(i, j) > 1000000:
                total += 1
    
    return total

if __name__ == '__main__':
    print(evaluate())