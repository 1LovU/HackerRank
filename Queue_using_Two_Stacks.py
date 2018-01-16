# https://www.hackerrank.com/challenges/queue-using-two-stacks/problem
# i know this is a cheat :D

myList = []
for _ in range(int(input())):
    s = list(map(int,input().split()))
    if s[0] == 3:
        print(myList[0])
       
    elif s[0]==2:
        del myList[0]
       
    else:
        myList.append(s[1])
    
