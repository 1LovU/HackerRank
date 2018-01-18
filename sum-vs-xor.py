# https://www.hackerrank.com/challenges/sum-vs-xor/problem

#!/bin/python3

import sys


n = int(input().strip())

zeros = (bin(n)[2:].count('0'))
count = 2**zeros
if n==0:
    count = 1
print(count)
