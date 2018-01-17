# https://www.hackerrank.com/challenges/palindrome-index/problem


#!/bin/python3

import sys

def checkPalin(s):
    n = len(s)
    for i in range(n//2):
        if s[i]!=s[n-i-1]:            
            return [i,n-i-1]
    return True



def palindromeIndex(s):
    index = checkPalin(s)
    if index == True:
        return -1    
    temp = list(s)
    del temp[index[0]]
    temp1 = list(s)
    del temp1[index[1]]
   
    if checkPalin(temp) is True:        
        return index[0]    
    elif checkPalin(temp1) is True:        
        return index[1]
    return -1
        
    

q = int(input().strip())
for a0 in range(q):
    s = input().strip()
    result = palindromeIndex(s)
    print(result)
