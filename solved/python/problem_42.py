import math


def load_names(filename) -> list[str]:
    with open(filename) as f:
        names = f.read().replace('"', "").split(",")
    return names


def evaluate_names(names: list[str]) -> int:
    amount = 0

    for name in names:
        val = 0
        for char in name:
            val += char_num(char)
        if untriangle(val) % 1 == 0:
            amount += 1

    return amount


def untriangle(num):
    return (-1 + math.sqrt(1 + (8 * num))) / 2


def char_num(char):
    return ord(char) - 64


if __name__ == "__main__":
    names = load_names("input.txt")
    print(evaluate_names(names))
