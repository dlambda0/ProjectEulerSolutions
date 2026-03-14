#!/usr/bin/env python3

from functools import reduce


def gen_intstr(num):
    intstr = ""
    
    for i in range(1, num):
        intstr += str(i)
        
    return intstr


def mult_digits(num, intstr):
    digit_list = []
    
    for i in range(1, num):
        digit = int(intstr[10 ** i])
        print(digit)
        digit_list.append(digit)
        
    return reduce(lambda x, y: x * y, digit_list)


if __name__ == '__main__':
    intstr = gen_intstr(10000000)
    answer = mult_digits(7, intstr)
    print(answer)