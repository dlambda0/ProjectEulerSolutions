#!/usr/bin/env python3


def is_palindrome(string):
    return string == string[::-1]

def flip_add(num):
    return num + int(str(num)[::-1])

def is_lychrel(num, iters=50):
    cur_num = num
    
    for i in range(iters):
        ans = flip_add(cur_num)
        if is_palindrome(str(ans)):
            return False
        else:
            cur_num = ans
            
    return True


def lychrel_check(end):
    lychrel_count = end
    
    for i in range(1, end + 1):
        if is_lychrel(i):
            continue
        else:
            lychrel_count -= 1
    
    return lychrel_count


if __name__ == '__main__':
    print(lychrel_check(10000))