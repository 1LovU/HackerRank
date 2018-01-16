# even this is a not the way it should be written, but if python handles it then why not
# https://www.hackerrank.com/challenges/qheap1/problem

from bisect import insort
n =  int(input())
myList = []
for _ in range(n):
    query =  input().split()
    
    if query[0]=='1':
        v = int(query[1])
        insort(myList,v)
        
    
    if query[0]=='2':
        v = int(query[1])
        myList.remove(v)
        
        
      
    if query[0]=='3':
        print(myList[0])
