# https://www.hackerrank.com/challenges/manasa-and-stones/problem


t = int(input().strip())
for _ in range(t):
    n = int(input().strip())    
    a = int(input().strip())
    b = int(input().strip())
    n-=1
    lastStone = set()
    for i in range(0,n+1):
        x = (i*a) + (n-i)*b
        lastStone.add(x)
    lastStone = list(lastStone)
    lastStone.sort()
    print(*lastStone)
        
