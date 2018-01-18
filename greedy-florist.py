# https://www.hackerrank.com/challenges/greedy-florist/problem

n,k = input().strip().split(' ')
n,k  = int(n),int(k)
f = list(map(int,input().strip().split(' ')))
f.sort()
f.reverse()
j=1
sum1 = 0
for i in range(n):
    if i!=0 and i%k==0:
        j+=1
    
    sum1= sum1+f[i]*j
print(sum1)
