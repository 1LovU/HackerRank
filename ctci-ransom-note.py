# https://www.hackerrank.com/challenges/ctci-ransom-note

from collections import defaultdict

def ransom_note(magazine, ransom):
    ranDict = defaultdict(int)
    for item in ransom:
        ranDict[item]-= 1
       
    for item in magazine:
        ranDict[item]+= 1
       
    for val in ranDict.values():
        if val < 0 :
            return False
       
    return True
        
    
    

m, n = map(int, input().strip().split(' '))
magazine = input().strip().split(' ')
ransom = input().strip().split(' ')
answer = ransom_note(magazine, ransom)
if(answer):
    print("Yes")
else:
    print("No")
    
