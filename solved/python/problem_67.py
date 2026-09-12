#!/usr/bin/env python3

def triangle_path_max(tri):
    for i in reversed(range(len(tri) - 1)):
        for j in range(len(tri[i])):
            tri[i][j] += max(tri[i + 1][j], tri[i + 1][j + 1])
    return tri[0][0]

def read_triangle(file):
    with open(file) as f:
        while True:
            return [
                [int(value) for value in line.split()]
                for line in f
                if line.strip()
            ]

if __name__ == '__main__':
    file = "input.txt"
    data = read_triangle(file)
    ans = triangle_path_max(data)
    print(ans)