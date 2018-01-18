# https://www.hackerrank.com/challenges/mars-exploration/problem

#!/bin/python3

import sys


S = input().strip()
sos = 'SOS'
count = 0
for i in range(len(S)):
    if S[i]!=sos[i%3]:
        count+=1
print(count)
