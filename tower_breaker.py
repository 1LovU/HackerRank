# https://www.hackerrank.com/challenges/tower-breakers-1/problem


for _ in range(int(input().strip())):
    n,m =  map(int,input().split())
    ans = 2 if (m == 1 or n % 2 == 0) else 1
    print(ans)
