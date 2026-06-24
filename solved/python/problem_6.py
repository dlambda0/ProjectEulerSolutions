#!/usr/bin/env python3

def sum_of_squares(max=10):
    ans = 0
    for num in range(max + 1):
        ans += num ** 2
    return ans
        

def square_of_sum(max=10):
    ans = 0
    for num in range(max + 1):
        ans += num
    return ans ** 2

if __name__ == '__main__':
    pos = 100
    difference = square_of_sum(pos) - sum_of_squares(pos)
    print(difference)