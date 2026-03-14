#!/usr/bin/env python3


def read_data(filename):
    pyramid = []

    with open(filename, "r") as f:
        data = f.readlines()

    for line in data:
        pyramid.append([int(x) for x in line.split()])

    return pyramid


def find_maxes(nums):
    return [max(x) for x in nums]

def find_max_indexes(nums):
    return [nums[x].index(max(nums[x])) for x in nums]


def max_path_sum(pyramid):
    answer = 0
    
    for row in pyramid:
        for element in row:
            pass
    
    return answer


if __name__ == "__main__":
    pyramid = read_data("input.txt")
    answer = find_max_indexes(pyramid)
    print(answer)
