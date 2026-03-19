#!/usr/bin/env python3


def brute_answer() -> int:
    for i in range(100000, 999999):
        if sort_digits(i) == sort_digits(i * 3) == sort_digits(i * 5):
            return i


def sort_digits(num: int) -> list[str]:
    return sorted(str(num))


if __name__ == "__main__":
    print(brute_answer())
