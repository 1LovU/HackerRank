# https://www.hackerrank.com/challenges/jumping-on-the-clouds/problem

#!/bin/python3

import sys


n = int(input().strip())
c = [int(c_temp) for c_temp in input().strip().split(' ')]
count = 0
i=0
while len(c)>2:
    if c[2]== 0:
        count+=1        
        c = c[2:]
    else:
        count+=1
        
        c = c[1:]
        
if len(c)==2:
    count+=1
        
print(count)    
    
