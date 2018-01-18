# https://www.hackerrank.com/challenges/xor-se/problem
# Surely got this logic from some comments 

def G(x):
    a = x % 8
    if(a == 0 or a == 1):
        return x
    if(a == 2 or a == 3):
        return 2
    if(a == 4 or a == 5):
        return x+2
    if(a == 6 or a == 7):
        return 0
    



Q = int(input().strip())
L  = []
R =  []
maxB = 0
for a0 in range(Q):
    a,b = input().strip().split(' ')
    a,b = [int(a),int(b)]    
    print(G(b) ^ G(a-1))
        
    
    
