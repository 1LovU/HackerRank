# https://www.hackerrank.com/challenges/anagram/problem

 # old logic.
 
 #!/bin/python3

import sys
from collections import defaultdict


def anagram(s):
    size = len(s)
    if size % 2 == 1:
        return -1
    mydict = defaultdict(int)
    for i in range(size//2):
        item = s[i]
        mydict[item]+=1
    for i in range(size//2,size):
        item = s[i]
        mydict[item]-=1
    count = 0
    for item in mydict.values():
        count += abs(item)
    return count//2
    
    
    

q = int(input().strip())
for a0 in range(q):
    s = input().strip()
    result = anagram(s)
    print(result)



