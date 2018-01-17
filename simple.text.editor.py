# -*- coding: utf-8 -*-
"""
Created on Wed Jun 28 12:27:25 2017

@author: amit.yadav

https://www.hackerrank.com/challenges/simple-text-editor
"""

class SimpleTextEditor:
    def __init__(self):
        self.myString = ''
        self.Stack = ['']
    
    def append(self,STR):
        self.myString = self.myString+STR
        self.updateStack()
        
    
    def delete(self,K):
        self.myString = self.myString[:-K]
        self.updateStack()
    
    def updateStack(self):
        self.Stack.append(self.myString)
    
    def undo(self): 
        del self.Stack[-1]
        self.myString = self.Stack[-1]
            
    
    def printK(self,K):
        print(self.myString[K-1])
        
        
if __name__ == '__main__':    
    String = SimpleTextEditor()    
    for _ in range(int(input())):        
        values = input().strip().split()
        if values[0] is '1':
            STR = values[1]
            String.append(STR)
        elif values[0] is '2':
            K = int(values[1])
            String.delete(K)
        elif values[0] is '3':
            K = int(values[1])
            String.printK(K)
        elif values[0] is '4':
            String.undo()
  
