#!/usr/bin/env python3


def chain_generator(num: int) -> list[int]:
    nums = [num]
    
    while nums[-1] != 1:
        if num % 2 == 0:
            num = num // 2
        else:
            num = (3 * num) + 1
        nums.append(num)
    
    return nums

def chain_length(num: int) -> int:
    return len(chain_generator(num))


if __name__ == '__main__':
    # kind of brute forced it here... but wherever!
    i = 900000
    highest = 0
    answer = 0
    for i in range(1, 999999):
        cur_length = chain_length(i)
        if cur_length > highest:
            highest = cur_length
            answer = i
            print(highest)
    print(f'ANSWER:{answer}')