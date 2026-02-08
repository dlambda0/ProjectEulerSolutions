#!/usr/bin/env python3


def gen_selfpower_series(end):
    series = 0
    
    for num in range(1, end + 1):
        series += num ** num
        
    return series


if __name__ == '__main__':
    print(gen_selfpower_series(1000))