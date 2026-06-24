#!/usr/bin/env python3

# can't believe I forgot about discrete math...
# I HATE COMBINATORICS

from math import comb


def grid_paths(grid_size: int) -> int:
    return comb(2 * grid_size, grid_size)


if __name__ == "__main__":
    answer = grid_paths(20)
    print(f'ANSWER: {answer}')
