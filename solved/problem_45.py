#!/usr/bin/env python3

# all hexagonal numbers are also triangular numbers

hex_num = lambda n: n * (2 * n - 1)

def pen_check(x):
    return ((1 + (1 + 24 * x) ** 0.5) / 6).is_integer()

def find_triple_match(hex_start):
    n = hex_start
    while True:
        h = hex_num(n)
        if pen_check(h):
            return h
        n += 1
        
    
    
if __name__ == '__main__':
    print(find_triple_match(144))