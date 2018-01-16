# https://www.hackerrank.com/challenges/ctci-balanced-brackets/problem

# Well, you dont always need the stack if u can code in better way :D

def is_matched(expression):
    while '[]' in expression or '{}' in expression or '()' in expression:
        expression = expression.replace('[]','')
        expression = expression.replace('{}','')
        expression = expression.replace('()','')
       
    if len(expression):
        return False
    return True
   
    

t = int(input().strip())
for a0 in range(t):
    expression = input().strip()
    if is_matched(expression) == True:
        print("YES")
    else:
        print("NO")
