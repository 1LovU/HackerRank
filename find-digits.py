# https://www.hackerrank.com/challenges/find-digits/problem


#!/bin/python3

import sys


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    nums = list(str(n))
    count = 0
    for item in nums:
        item  =  int(item)
        if item !=0:
            if n % item ==0:
                count +=1
    print(count)
        
