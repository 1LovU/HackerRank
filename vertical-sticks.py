# https://www.hackerrank.com/challenges/vertical-sticks/problem
# logic :: https://cs.stackexchange.com/a/1114


t =  int(input().strip())
for _ in range(t):
    n = int(input().strip())
    v = list(map(int,input().strip().split(' ')))
    counter = [0]*n
    for i in range(len(v)):
        for j in range(len(v)):
            if v[i]<=v[j]:
                counter[i]+=1
    final = 0
    for i in range(len(counter)):
        final += 1/(counter[i]+1)
    
    answer = (n+1)*final
    answer = float(round(answer, 2))
    print("{:0.2f}".format(answer))
                
             
    
