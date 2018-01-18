# https://www.hackerrank.com/challenges/counting-valleys/problem

n = int(input())
steps = input()
level = 0
valley = 0
for ch in steps:
    if ch == 'U':
        level += 1
        if level == 0:
            valley += 1
    else:
        level -= 1
print(valley)
