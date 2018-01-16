# https://www.hackerrank.com/challenges/median/problem
def Mid(a,size):
            if size == 0:
                return ('Wrong!')
            
            elif (size) % 2 == 1:
                return (a[size//2])

            else:
                mid = (a[size//2]+a[size//2-1])/2.0
                if mid ==  int(mid):
                    mid = int(mid)
                return (mid)


from bisect import insort ,  bisect_left
from collections import defaultdict

N = int(input())
a = []
myDict = defaultdict(int)
for i in range(N):
    q,val = input().strip().split(' ')
    val = int(val)
    
    
    if q == 'r':
        if myDict[val] == 0:
            print('Wrong!')
           
        else:
            myDict[val] -= 1
            index = bisect_left(a,val)
            del a[index]
            size = len(a)
            print(Mid(a,size))

           
       
    else:
        insort(a, val)
        size = len(a)
        myDict[val] += 1   
        print(Mid(a,size))
        
