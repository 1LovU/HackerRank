# https://www.hackerrank.com/challenges/utopian-tree/problem

#!/bin/python3

import sys


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    x = 1
    for i in range(1,n+1):
        if i % 2 ==1:
            x = x*2
        else:
            x += 1
        
    
    print(x)
