# https://www.hackerrank.com/challenges/ctci-big-o/problem

from math import ceil 
def checkPrime(n):
    mid =  ceil(n**(1/2))+1
    if n <= 1:
        return 'Not prime'        
    if n == 2:
        return 'Prime'
    if n % 2 == 0:
        return 'Not prime'
    
    for i in range(3,mid,2):       
        if n % i == 0:
            return 'Not prime'       
    return 'Prime'


p = int(input().strip())
for a0 in range(p):
    n = int(input().strip())
    print(checkPrime(n))
