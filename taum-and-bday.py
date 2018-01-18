# https://www.hackerrank.com/challenges/taum-and-bday/problem

def orig(b,w,x,y):
    return b*x+w*y

def exchB2W(b,w,x,y,z):
    a1 = b*x+w*(x+z)   
    a2 = b*(y+z)+w*y    
    return min(a1,a2)

t = int(input().strip())
for a0 in range(t):
    b,w = input().strip().split(' ')
    b,w = [int(b),int(w)]
    x,y,z = input().strip().split(' ')
    x,y,z = [int(x),int(y),int(z)]
    original = orig(b,w,x,y)
    exchangeB2W = exchB2W(b,w,x,y,z)
       
    print(min(original,exchangeB2W))
    
