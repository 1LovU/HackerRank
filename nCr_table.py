# https://www.hackerrank.com/challenges/ncr-table/problem



import math
def nCr(n,r):
    f = math.factorial
    return ((f(n) // f(r) // f(n-r))%(10**9))

if __name__ == '__main__':
    t = int(input().strip())
    for _ in range(t):
        n = int(input().strip())
        for i in range(0,n+1):
            print(nCr(n,i),end=' ')
        print()
