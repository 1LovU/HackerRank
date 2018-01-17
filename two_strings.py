# https://www.hackerrank.com/challenges/two-strings/problem

#!/bin/python3

import sys

def twoStrings(s1, s2):
    for item in s1:
        if item in s2:
            return 'YES'
    return 'NO'
    

q = int(input().strip())
for a0 in range(q):
    s1 = input().strip()
    s2 = input().strip()
    result = twoStrings(s1, s2)
    print(result)
