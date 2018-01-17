# https://www.hackerrank.com/challenges/climbing-the-leaderboard/problem

n = int(input().strip())
scores = [int(scores_temp) for scores_temp in input().strip().split(' ')]
m = int(input().strip())
alice = [int(alice_temp) for alice_temp in input().strip().split(' ')]

scores = list(set(scores))
scores.sort()
size =  len(scores)

i=0
k=0
while i < len(alice):
    if alice[i]>=scores[-1]:
        print(1)       
        
    else:
        while scores[k] <= alice[i]:
            k+=1  
            if k >= size:
                break
        print(size+1-k)
    i+=1
    
    
            
        
