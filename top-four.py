# https://www.hackerrank.com/challenges/top-four

N = int(raw_input())
myStack = []
for _ in range(N):
    number = int(raw_input())
    myStack.append(number)
    
        
        

myStack.sort()
for i in range(-1,-5,-1):
    print myStack[i]
