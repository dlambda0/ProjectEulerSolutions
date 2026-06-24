#!/usr/bin/env python3

def fibonacci_index():
    n1 = 1
    n2 = 1
    steps = 2
    while len(str(n2)) < 1000:
        temp = n1 + n2
        n1 = n2
        n2 = temp
        steps += 1
        
    return steps
        

if __name__ == '__main__':
    print(fibonacci_index())