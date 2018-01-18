# https://www.hackerrank.com/challenges/beautiful-triplets/problem

n,d = input().strip().split(' ')
n,d = int(n),int(d)
c  = list(map(int,input().strip().split(' ')))        # Better use set here
count = 0
for i in range(n):
    if c[i]+d in c and c[i]+2*d in c:
        count+=1

print(count)
