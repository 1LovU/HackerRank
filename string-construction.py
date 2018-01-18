# https://www.hackerrank.com/challenges/string-construction/problem

#!/bin/python3

import sys


n = int(input().strip())

for a0 in range(n):
    p = []
    count = 0
    s = input().strip()
    for i in range(len(s)):
        if s[i] in p:
            p.append(s[i])
        else:
            p.append(s[i])
            count+=1
    print(count)
            
