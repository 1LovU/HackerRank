# https://www.hackerrank.com/challenges/sherlock-and-valid-string/problem
# surely a very old logic :D

s =  input().strip()

counter = [0]*26
for i in range(len(s)):
    counter[ord(s[i])-97]+=1
count = 0
counter = [x for x in counter if x != 0]
countSet = set(counter)

    
from collections import Counter 

Maxcount = Counter(counter).most_common()
if len(Maxcount)==1:
    print('YES')
elif Maxcount[1][1] > 1 or len(Maxcount)>2 :
    print('NO')
else:
    print('YES')
