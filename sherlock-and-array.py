# https://www.hackerrank.com/challenges/sherlock-and-array/problem

#!/bin/python3

import sys

def solve(a):
    if len(a)==1:
        return 'YES'
    
    leftSum = 0
    RightSum = sum(a)-a[0]
    pivot =  a[0]
    
    for i in range(0,len(a)-1):
        leftSum += pivot
        pivot = a[i+1]
        RightSum -= pivot       
        
        if leftSum == RightSum:
            return 'YES'
    return 'NO'
    

T = int(input().strip())
for a0 in range(T):
    n = int(input().strip())
    a = list(map(int, input().strip().split(' ')))
    result = solve(a)
    print(result)
