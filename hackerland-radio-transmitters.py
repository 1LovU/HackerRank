# https://www.hackerrank.com/challenges/hackerland-radio-transmitters/problem

# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 22:13:05 2017

@author: amit.yadav
"""

n,k = input().strip().split(' ')
n,k = [int(n),int(k)]
x = [int(x_temp) for x_temp in input().strip().split(' ')]

x.sort()
count = 0
i = 0
while (i < n):
    count+=1
    loc = x[i] + k
    while (i < n and x[i] <= loc):
        i+=1
    i-=1   
    loc = x[--i] + k
    while (i < n and x[i] <= loc):
        i+=1

print(count)
