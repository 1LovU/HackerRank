# https://www.hackerrank.com/challenges/alternating-characters/problem

#!/bin/python3

import sys

def alternatingCharacters(s):
    count = 0
    for i in range(len(s)-1):
        if s[i]==s[i+1]:
            count+=1
    return count
    
    
q = int(input().strip())
for a0 in range(q):
    s = input().strip()
    result = alternatingCharacters(s)
    print(result)
