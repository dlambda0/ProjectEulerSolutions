#!/usr/bin/env python3


def triangle_number_list(amount) -> list[int]:
    return [n * (n + 1) // 2 for n in range(1, amount + 1)]


def amount_divisible(triangle_numbers: list[int], divisors: int=500) -> int:
    for n in triangle_numbers:
        if divisor_counter(n) > divisors:
            return n
    return None


def divisor_counter(number: int) -> int:
    count = 0
    i = 1
    while i * i <= number:
        if number % i == 0 :
            if i * i == number:
                count += 1
            else:
                count += 2
        i += 1
    return count

if __name__ == '__main__':
    nums = triangle_number_list(20000)
    answer = amount_divisible(nums)
    print(f'ANSWER: {answer}')
    