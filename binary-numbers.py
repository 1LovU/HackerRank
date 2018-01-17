# https://www.hackerrank.com/challenges/linkedin-practice-binary-numbers/problem

#!/bin/python3

import sys


n = int(input().strip())
b = bin(n)[2:]
max_count = 0

i = 0
while i<len(b):
    count = 0
    while b[i]=='1':
        count+=1
        i+=1
        if i >= len(b):
            break
    if count>max_count:
        max_count = count
    i+=1
print(max_count)
    
    
