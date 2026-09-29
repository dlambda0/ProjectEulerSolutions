#!/usr/bin/env python3
 
def abundant_nums(lim):
    divisor_sum = [0] * lim
    for i in range(1, lim):
        for j in range(i * 2, lim, i):
            divisor_sum[j] += i
    return [i for (i, x) in enumerate(divisor_sum) if x > i] 

def expressable_nums(lim, nums):
    expressable = [False] * lim
    for i in nums:
        for j in nums:
            if i + j < lim:
                expressable[i + j] = True
            else:
                break
    return expressable

if __name__ == "__main__":
    LIM = 28124
    abund = abundant_nums(LIM)
    expr = expressable_nums(LIM, abund)
    ans = sum(i for (i, x) in enumerate(expr) if not x)
    print(ans)