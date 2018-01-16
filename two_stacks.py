# https://www.hackerrank.com/challenges/ctci-queue-using-two-stacks/problem

class MyQueue(object):
    def __init__(self):
        self.MyList = []
        
    
    def peek(self):
        return self.MyList[0]
        
    def pop(self):
        del self.MyList[0]
        
        
        
    def put(self, value):
        self.MyList.append(value)
        

queue = MyQueue()
t = int(input())
for line in range(t):
    values = map(int, input().split())
    values = list(values)
    if values[0] == 1:
        queue.put(values[1])        
    elif values[0] == 2:
        queue.pop()
    else:
        print(queue.peek())
        
