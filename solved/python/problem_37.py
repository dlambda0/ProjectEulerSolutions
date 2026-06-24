#!usr/bin/env python3

from sympy import isprime


def is_truncatable(num: int):
    num_str = str(num)
    
    for i in range(len(num_str)):
        truncated = int(num_str[:len(num_str)-i])
        if not isprime(truncated):
            return False
    
    for i in range(len(num_str)):
        truncated = int(num_str[i:])
        if not isprime(truncated):
            return False
        
    return True


def find_truncatable(limit: int) -> list:
    truncatable_primes = []
    num = 11 # to speed things up
    
    # just adding and checking should work?
    while len(truncatable_primes) < limit:
        if isprime(num) and is_truncatable(num):
            truncatable_primes.append(num)
        num += 1
        
    return truncatable_primes


if __name__ == '__main__':
    places = 11
    answer = sum(find_truncatable(places))
    print(f'at {places} the answer is {answer}')
    
