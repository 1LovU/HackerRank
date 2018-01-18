# https://www.hackerrank.com/challenges/30-review-loop/problem


T =  int(input().strip())
for _ in range(T):
    s = input().strip()
    for i in range(len(s)):
        if i%2 == 0:
            print(s[i],end='')
    print(' ',end='')
    for i in range(len(s)):
        if i%2 == 1:
            print(s[i],end='')
    print()
