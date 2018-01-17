# https://www.hackerrank.com/challenges/mark-and-toys/problem

n,m = input().strip().split()
n,m = int(n),int(m)
ToyPrices =  list(map(int,input().strip().split()))
ToyPrices.sort()

count = 0
i = 0
while True:
    m-=ToyPrices[i]
    i+=1
    if m<=0:
        break
    count+=1
print(count)
