# https://www.hackerrank.com/challenges/game-of-throne-ii/problem

from collections import defaultdict
from math import factorial 
def checkPalin(s):
    setS = list(set((s)))     
    count  = 0
    for i in setS:
        if s.count(i)%2==1:
            count+=1
        if count > 1:
            return False
    return True
    
def countPalin(s):
    counter = defaultdict(int)
    for item in s:
        counter[item] += 1
    n = len(s)//2
    ans = factorial(n)
    
    for val in counter.values():
        ans //= factorial(val//2)
        
    return int(ans % MOD)
        
    

MOD = (10**9 + 7)
s = input().strip()
if checkPalin(s):
    print(countPalin(s))
else:
    print(0)

