#!/usr/bin/env python3

def gen_numstr():
    numstr = ""
    
    for i in range(1, 1000000):
        numstr += str(i)
        
    return numstr

def evaluate(numstr):
    return (int(numstr[0]) * int(numstr[9]) * int(numstr[99]) * int(numstr[999]) * int(numstr[9999]) * int(numstr[99999]) * int(numstr[999999]))


if __name__ == '__main__':
    print(evaluate(gen_numstr()))