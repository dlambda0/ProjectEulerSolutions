#!/usr/bin/env python3


def read_data(filename):
    pyramid = []
    
    with open(filename, 'r') as f:
        data = f.readlines()
    
    for line in range(len(data)):
        str_nums = line.split()
        for str_num in str_nums:
            int_num = int(str_num)
            
            pyramid[line].append(int_num)
            
    return pyramid

def brute_force_paths(pyramid):
    for row in range(len(pyramid) - 1):
        for col in range(len(pyramid[row])):
            
            


if __name__ == '__main__':
    pyramid = read_data('data/problem_18.txt')
    brute_force_paths(pyramid)
    print(max(pyramid[-1]))