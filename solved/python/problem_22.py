#!/usr/bin/env python3


def load_names(filename):
    with open(filename, "r") as file:
        file_str = file.readline()

    return sorted(file_str.replace('"', "").split(","))


def score_name(name):
    return sum([(ord(char) - 64) for char in name])


def score_name_list(namelist):
    score = 0
    
    for i, name in enumerate(namelist, start=1):
        score += score_name(name) * i
        
    return score


if __name__ == "__main__":
    names = load_names('names.txt')
    score = score_name_list(names)
    print(score)
