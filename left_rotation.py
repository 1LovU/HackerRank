# https://www.hackerrank.com/challenges/array-left-rotation/problem
# very old code, not sure if good or not.

def array_left_rotation(a, n, k):
    if n == k:
        return a
    else:     
        b = []
        for i in range(k,n):
            b.append(a[i])
        for i in range(0,k):
            b.append(a[i])
    return b
            
            
    

n, k = map(int, input().strip().split(' '))
a = list(map(int, input().strip().split(' ')))
answer = array_left_rotation(a, n, k);
print(*answer, sep=' ')
