# https://www.hackerrank.com/challenges/ctci-recursive-staircase/problem

def get_mod_fib(n):
    f1, f2, f3 = 1, 2, 4
    for i in range(n-1):
        f1, f2, f3 = f2, f3, f1 + f2 + f3
    return f1

s = int(input().strip())
for a0 in range(s):
    n = int(input().strip())
    print(get_mod_fib(n))
