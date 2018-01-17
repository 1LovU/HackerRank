# https://www.hackerrank.com/challenges/caesar-cipher-1
# old logic, may be using DICT can improve the code.
#!/bin/python3

import sys


n = int(input().strip())
s = input().strip()
k = int(input().strip())
s = list(s)
k = k%26

for i in range(n):
    if s[i].isalpha():
        if s[i].islower():
            if ord(s[i])+k > ord('z'):
                s[i] = chr(ord('a')-1+k-ord('z')+ord(s[i]))
            else:
                s[i] = chr(ord(s[i])+k)
        else:
            if ord(s[i])+k > ord('Z'):
                s[i] = chr(ord('A')-1+k-ord('Z')+ord(s[i]))
            else:
                s[i] = chr(ord(s[i])+k)
print(''.join(s))
                
                


