#!/usr/bin/env python3

def gen_powerlist(max):
    pow_set = set()
    
    for a in range(2, max):
        for b in range(2, max):
            pow_set.add(a ** b)
    
    return pow_set

if __name__ == '__main__':
    pow_list = gen_powerlist(101)
    print(len(pow_list))