# https://www.hackerrank.com/challenges/missing-numbers/problem

from collections import defaultdict
myDict =  defaultdict(int)     # u can use Counter here..

n = int(input())
A = list(input().split())
m = int(input())
B = list(input().split())

for i in range(m):
    if i < n:
        myDict[A[i]] -= 1
    myDict[B[i]] += 1
myList= [key for key,val in myDict.items() if val > 0 ]
myList.sort()
print(*myList)
    
       
    
        
