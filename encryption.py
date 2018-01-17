# https://www.hackerrank.com/challenges/encryption/problem

import math


s = list(input().strip())
L =  len(s)
row = math.floor(L**(1/2))
col = math.ceil(L**(1/2))

for i in range(col):
    x = 0     
    while True:
        try:
            print(s[i+x],end='')
            x+= col
        except:
            break
        
    print(' ',end='')
    
