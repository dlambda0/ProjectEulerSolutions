#!/usr/bin/env python3

import itertools

# yup, im lazy

if __name__ == '__main__':
    nums = list(range(10))
    permutes_list = list(itertools.permutations(nums))
    print(permutes_list[999999])