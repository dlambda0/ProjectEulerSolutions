#!/usr/bin/env python3

from functools import reduce


def load_integers(filename) -> list[int]:
    with open(filename, "r") as file:
        numbers = file.read().strip().replace("\n", "")
    return [int(num) for num in numbers]


def product(nums: list[int], start: int, places: int) -> int:
    return reduce(lambda x, y: x * y, nums[start : places + start])


if __name__ == "__main__":
    places = int(input())  # number of places to determine
    numbers = load_integers("data.txt")
    biggest = 0
    
    for start in range(len(numbers) - places + 1):
        answer = product(numbers, start, places)
        if answer > biggest:
            biggest = answer
            print(biggest)
            
    print(f"ANSWER: {biggest}")
