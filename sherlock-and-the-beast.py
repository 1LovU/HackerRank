# https://www.hackerrank.com/challenges/sherlock-and-the-beast/problem

def decentNum(N):
    if N < 3:
        return [-1]
    if N % 3 == 0:
        return [5]*N    
    for i in range(1,N+1):
        if (N-i)%3 ==0 and i%5 == 0:
            return [5]*(N-i)+[3]*i
    for i in range(1,N+1):
        if (N-i)%5 ==0 and i%3 == 0:
            return [3]*(N-i)+[5]*i
    return [-1]
     
    
    
if __name__ == '__main__':
    t = int(input().strip())
    for a0 in range(t):
        N = int(input().strip())
        print(*decentNum(N),sep='')
