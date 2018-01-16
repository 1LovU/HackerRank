# you need to love the bisect module for many reasons :P
# https://www.hackerrank.com/challenges/find-the-running-median/problem


import sys
import bisect
n = int(input().strip())
a = []

for i in range(n):
    a_t = int(input().strip())
    bisect.insort(a, a_t)
    if (i+1) % 2 == 1:
        print(a[i//2]/1.0)
       
    else:
        mid = (a[i//2]+a[i//2+1])/2.0
        print(mid)
