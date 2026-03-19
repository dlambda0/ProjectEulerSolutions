#!/usr/bin/env python3


def read_data(filename):
    pyramid = []

    with open(filename, "r") as f:
        data = f.readlines()

    for line in data:
        pyramid.append([int(x) for x in line.split()])

    return pyramid


def row_max_indexes(pyramid):
    return [x.index(max(x)) for x in pyramid]

def calc_answer(pyramid):
    return sum([])

if __name__ == "__main__":
    pyramid = read_data("input.txt")
    print(row_max_indexes(pyramid))
