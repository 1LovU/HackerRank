# https://www.hackerrank.com/challenges/maximum-element/problem

class Stack:
    def __init__(self):        
        self.MaxStack = [0]
        self.curMax = 0
        
    def push(self,val):        
        self.curMax = max(val,self.curMax)
        self.MaxStack.append(self.curMax)
    
    def pop(self): 
        del self.MaxStack[-1] 
        self.curMax = self.MaxStack[-1]

    def prints(self):        
        print(self.curMax)
        
        
        
if __name__ == '__main__':
    myStack = Stack()
    N =  int(input().strip())
    for _ in range(N):
        temp = input().split()
        if temp[0]=='3':
            myStack.prints()
            
        if temp[0]=='1':
            val = int(temp[1])
            myStack.push(val)
        
        if temp[0]=='2':            
            myStack.pop()
            
            
            
    
        
            
            
        
        
            
        
        
   
