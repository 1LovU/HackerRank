# https://www.hackerrank.com/challenges/uk-and-us-2

n =  int(input().strip())
s = ''
for _ in range(n):
    s+= ' '+(input().strip())
   
s = s.split(' ')
t = int(input().strip())

for i in range(t):
    totalCount = 0
    word = input().strip()
    word1 = word.replace('our','or')
    for item in s:
        if word == item or word1 ==  item:
            totalCount+=1
            
    print(totalCount)
    
