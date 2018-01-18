# https://www.hackerrank.com/challenges/apple-and-orange/problem
# why am i posting this ?  :D


#!/bin/python3

import sys


s,t = input().strip().split(' ')
s,t = [int(s),int(t)]
a,b = input().strip().split(' ')
a,b = [int(a),int(b)]
m,n = input().strip().split(' ')
m,n = [int(m),int(n)]
apple = [int(apple_temp) for apple_temp in input().strip().split(' ')]
orange = [int(orange_temp) for orange_temp in input().strip().split(' ')]
count_apples = 0
count_orange = 0
for i in apple:
    if ((a+i) >= s) and  ((a+i) <= t):        
        count_apples+=1
for i in orange:
    if ((b+i) >= s) and  ((b+i) <= t):
        count_orange+=1
print(count_apples)
print(count_orange)
