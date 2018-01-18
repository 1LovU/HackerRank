https://www.hackerrank.com/challenges/strange-code/problem
# Logic from some comments 

t =  int(input().strip())

rem = 3
while t > rem:
    t = t-rem
    rem *= 2

print(rem-t+1)
