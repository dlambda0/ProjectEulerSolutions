#!/usr/bin/env python3

import datetime

def count_first_sundays(start_year=1901, end_year=2000):
    
    count = 0
    
    for year in range(start_year, end_year + 1):
        for month in range(1, 13):
            first_day = datetime.date(year, month, 1)
            
            if first_day.weekday() == 6:
                count += 1

    return count

if __name__ == '__main__':
    print(count_first_sundays())