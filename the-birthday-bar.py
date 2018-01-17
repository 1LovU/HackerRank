# https://www.hackerrank.com/challenges/the-birthday-bar/problem


#!/bin/python3

import sys

def getWays(squares, d, m): 
    count = 0    
    for i in range(0,n+1-m):
        if sum(squares[i:i+m]) == d:
            count+=1
    return count
       
    

n = int(input().strip())
s = list(map(int, input().strip().split(' ')))
d,m = input().strip().split(' ')
d,m = [int(d),int(m)]
result = getWays(s, d, m)
print(result)
