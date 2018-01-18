# https://www.hackerrank.com/challenges/jumping-on-the-clouds-revisited/problem


#!/bin/python3

import sys


n,k = input().strip().split(' ')
n,k = [int(n),int(k)]
c = [int(c_temp) for c_temp in input().strip().split(' ')]
sum1= 0
for i in range(0,n,k):
    sum1 =  sum1 + c[i]
red_2 = sum1 *2
jumps = n/k

print(int(100-red_2-jumps))
    
