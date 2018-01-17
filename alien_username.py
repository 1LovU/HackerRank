
# https://www.hackerrank.com/challenges/alien-username/problem

def CheckAlien(s):
    if len(s) == 1:
        return 'INVALID'
        
    term = False
    num =  True
    alpha = False
    if s[0]!= '_' and s[0]!='.':
        return 'INVALID'
    if s[1].isnumeric() == False:
        return 'INVALID'
    if s[-1] == '_':
        term = True
       
    if not s[-1].isnumeric() and not s[-1].isalpha() and s[-1] != '_':
        return 'INVALID'
      
    for i in range(2,len(s)):
        if not s[i].isnumeric() and not s[i].isalpha() and i < len(s)-1:
            return 'INVALID'
        if alpha and not term:
            if s[i].isnumeric():
                return 'INVALID'
            
        if s[i].isalpha():
            alpha = True
           
       
    return 'VALID'
            
 



for _ in range(int(input())):
    s =  input()
    print(CheckAlien(s))
