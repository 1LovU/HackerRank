# https://www.hackerrank.com/challenges/crush/problem

n,m = input().strip().split(' ')
n,m = int(n),int(m)
mylist = [0] * (n+1)
while(m):
    m-=1
    a,b,k = input().strip().split(' ')
    a,b,k = int(a),int(b),int(k)
    mylist[a-1]+=k
    mylist[b]-=k
maxSum = 0 
x = 0
for item in (mylist):
    x += item
    if x > maxSum:
        maxSum = x
print(maxSum)    
    
    
