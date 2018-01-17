# https://www.hackerrank.com/challenges/luck-balance

n,k= input().strip().split()
n,k = int(n),int(k)
count = 0
impContest = []
for _ in range(n):
    L,T = input().strip().split()
    L,T = int(L),int(T)
    if T == 0:
        count += L
    else:
        impContest.append(L)
impContest.sort()
size = len(impContest)-k
newList = impContest[size:]
luckNegative = impContest[:size]
count+= sum(newList) - sum(luckNegative)

if size < 0:
    print(count+sum(impContest)-sum(newList)+sum(luckNegative))
else:
    print(count)
        
        
    
    
    
