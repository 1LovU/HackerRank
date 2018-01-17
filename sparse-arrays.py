# https://www.hackerrank.com/challenges/sparse-arrays/problem
# can be done using Counter from collections // its been starting days of coding :D

myDict = dict()
for _ in range(int(input())):
    s = input().strip()
    if s in myDict:
        myDict[s]+=1
    else:
        myDict[s] = 1
for _ in range(int(input())):
    s = input().strip()
    print(myDict.get(s,0))
