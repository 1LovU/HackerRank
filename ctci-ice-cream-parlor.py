# https://www.hackerrank.com/challenges/ctci-ice-cream-parlor


t = int(input().strip())
for a0 in range(t):
    m = int(input().strip())
    n = int(input().strip())
    a = list(map(int, input().strip().split(' ')))
    flag = 1
    for i in range(0,n):
        for j in range(i+1,n):
            if a[i]+a[j]==m:
                print(i+1,j+1)
                flag = 0
                break
        if flag == 0:
            break
