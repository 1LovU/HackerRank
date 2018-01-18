# https://www.hackerrank.com/challenges/between-two-sets/problem


# No idea what i did here :D

#!/bin/python3

import sys


n,m = input().strip().split(' ')
n,m = [int(n),int(m)]
a = [int(a_temp) for a_temp in input().strip().split(' ')]
b = [int(b_temp) for b_temp in input().strip().split(' ')]
count = 0
for i in range(max(a),min(b)+1):
    flag  = 0
    for item in a:
        if i % item !=0:
            flag = 1
            break
    if flag == 0:
        for item in b:
            if item % i !=0:
                flag=1
                break
    if flag == 0:
        count+=1
print(count)
      
    
