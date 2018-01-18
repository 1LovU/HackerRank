# https://www.hackerrank.com/challenges/sherlock-and-squares/problem

# Dont mind my old approach :D

# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 01:17:25 2017

@author: amit.yadav
"""

def SquareCount(start,end):    
    count  = 0
    flag = 1
    pivot  = start**(1/2)
    if start == end:
        flag = 0
    if pivot == int(start **(1/2)):            # perfect square
        pivot = pivot
        count1=1
    else:
        pivot = int(pivot)
        pivot +=1
        count1 = 0
    if flag == 0:
        return count1
    while(True):
        if pivot**2<=end:
            count+=1
            pivot+=1        
        else:
            break           
    return count


T =  int(input().strip())
for _ in range(T):
    count = 0
    first,last  =  input().strip().split(' ')
    first,last  = int(first),int(last)     
            
    print(SquareCount(first,last))
    
    
