#!/usr/bin/env python3


# the words lol
SINGLE = [
    "zero",
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
    "ten",
    "eleven",
    "twelve",
    "thirteen",
    "fourteen",
    "fifteen",
    "sixteen",
    "seventeen",
    "eighteen",
    "nineteen",
]
DOUBLE = [
    "",  # empty for 0 and 1
    "",
    "twenty",
    "thirty",
    "forty",
    "fifty",
    "sixty",
    "seventy",
    "eighty",
    "ninety",
]


def num_to_english(num):
    if 0 <= num < 20:
        return SINGLE[num]
    if 20 <= num < 100:
        return DOUBLE[num // 10] + (SINGLE[num % 10] if (num % 10 != 0) else "")
    if 100 <= num < 1000:
        return SINGLE[num // 100] + "hundred" + (("and" + num_to_english(num % 100)) if (num % 100 != 0) else "")
    if num == 1000:
        return "onethousand"


def sum_of_numwords(max):
    return sum(len(num_to_english(i)) for i in range(1, max + 1))


def test_translation():
    if num_to_english(15) != "fifteen":
        raise "FAILED 15"
    if num_to_english(78) != "seventyeight":
        raise "FAILED 78"
    if num_to_english(575) != "fivehundredandseventyfive":
        raise "FAILED 575"


if __name__ == "__main__":
    print(sum_of_numwords(1000))
