# https://www.hackerrank.com/challenges/flipping-bits/problem

t =  int(input().strip())
for _ in range(t):
    n = int(input().strip())
    x = 11111111111111111111111111111111
    n = int(bin(n)[2:])
    y = (x-n)
    print(int(str(y), 2))
