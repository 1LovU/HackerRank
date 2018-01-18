# https://www.hackerrank.com/challenges/halloween-party/problem

t =  int(input().strip())
for _ in range(t):
    n = int(input().strip())
    if n % 2 == 0:
        print((n//2)**2)
    else:
        print((n//2)*(n//2+1))
