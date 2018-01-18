# https://www.hackerrank.com/challenges/electronics-shop/problem

#!/bin/python3

import sys


s,n,m = input().strip().split(' ')
s,n,m = [int(s),int(n),int(m)]
keyboards = [int(keyboards_temp) for keyboards_temp in input().strip().split(' ')]
pendrives = [int(pendrives_temp) for pendrives_temp in input().strip().split(' ')]

max_price = -1
for i in range(0,len(keyboards)):
    for j in range(0,len(pendrives)):
        if keyboards[i]+pendrives[j] == s:
            max_price = s
            break
        elif ((keyboards[i]+pendrives[j]) < s) and ((keyboards[i]+pendrives[j]) > max_price):
            max_price = keyboards[i]+pendrives[j]
    if max_price == s:
        break
print(max_price)
