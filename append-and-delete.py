# https://www.hackerrank.com/challenges/append-and-delete/problem

#!/bin/python3

import sys


s = input().strip()
t = input().strip()
k = int(input().strip())

i =0
if s==t:
    i = len(s)
else:
    while(s[0:i]==t[0:i]):
        i+=1
commonLength = i-1 
sLen =  len(s)
tLen = len(t)

if((sLen+tLen-2*commonLength)>k):
    print("No")
elif((sLen+tLen-2*commonLength)%2==k%2):
    print("Yes")

elif ((sLen+tLen-k)<0):
    print("Yes")

else:
    print("No")
     
