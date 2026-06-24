#!/usr/bin/env python3

from math import prod

def gridize(filename) -> list:
    matrix = []
    
    with open(filename, 'r') as file:
        for line in file:
            matrix.append([int(num) for num in line.split()])
            
    return matrix

def find_max_line(grid: list) -> int:
    max_product = 0
    grid_size = len(grid)
    
    # right
    for i in range(grid_size):
        for j in range(grid_size - 3):
            product = prod(grid[i][j : j + 4])
            if product > max_product: max_product = product
    
    # diagonal right
    for i in range(grid_size - 3):
        for j in range(grid_size - 3):
            product = prod([grid[i + k][j + k] for k in range(4)])
            if product > max_product: max_product = product

    # down
    for i in range(grid_size - 3):
        for j in range(grid_size):
            product = prod([grid[i + k][j] for k in range(4)])
            if product > max_product: max_product = product
            
    # diagonal left 
    for i in range(grid_size - 3):
        for j in range(3, grid_size):
            product = prod([grid[i + k][j - k] for k in range(4)])
            if product > max_product: max_product = product
            
    return max_product


if __name__ == '__main__':
    answer = find_max_line(gridize('data.txt'))
    print(f'ANSWER: {answer}')