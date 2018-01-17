# https://www.hackerrank.com/challenges/word-order/problem

from collections import OrderedDict

myDict= OrderedDict()

for _ in range(int(input())):
    word = input().strip()
    
    myDict[word] = myDict.get(word,0) + 1

   
print(len(myDict))
print(*myDict.values())
