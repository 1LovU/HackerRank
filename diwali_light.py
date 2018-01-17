# https://www.hackerrank.com/challenges/diwali-lights/problem
for _ in range(int(input())):
    num = int(input())
    ans = (2**num-1) % 100000
    print(ans)
