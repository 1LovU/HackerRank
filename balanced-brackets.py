# https://www.hackerrank.com/challenges/balanced-brackets/problem
# why u need stack :D

#!/bin/python3

import sys


t = int(input().strip())
for a0 in range(t):
    s = input().strip()
    braces = ['{}','()','[]']
    while s:
        if (braces[0] in s or braces[1] in s or braces[2] in s):
            s = s.replace('()','')
            s = s.replace('{}','')
            s = s.replace('[]','')           
        
        else:
            print('NO')
            break
            
    if not s:
        print ('YES')


