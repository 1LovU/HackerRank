# https://www.hackerrank.com/challenges/acm-icpc-team/problem

#!/bin/python3


n,m = input().strip().split(' ')
n,m = [int(n),int(m)]
topic = []
topic_i = 0
for topic_i in range(n):
    topic_t = str(input().strip())
    topic.append(topic_t)
max_val = 0

for i in range(n):
    for j in range(i+1,n):
        val = int(topic[i],2) | int(topic[j],2)
        cur_max = bin(val).count('1')
        if max_val < cur_max:
            max_val = cur_max            
            count = 1

        elif max_val == cur_max:
            count += 1
print(max_val)
print(count)

        
        
