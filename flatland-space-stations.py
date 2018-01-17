# https://www.hackerrank.com/challenges/flatland-space-stations/problem



#!/bin/python3

import sys


n,m = input().strip().split(' ')
n,m = [int(n),int(m)]
c = [int(c_temp) for c_temp in input().strip().split(' ')]

myCity = [0]*n
for item in c:
    myCity[item] += 1
count = 0
cityString = ''.join(map(str, myCity))
cityList = cityString.split('1')
for i in range(len(cityList)):
    pivot = len(cityList[i])
    if pivot > count:
        count = pivot
count = (count+1)//2



print(max(len(cityList[0]),len(cityList[-1]),count))
        
    
    
