
# https://www.hackerrank.com/challenges/priyanka-and-toys/problem

size = int(input().strip())
toys = list(map(int, input().strip().split()))
counter = [0]*(max(toys)+1)
count = 0
i = 0
for item in toys:
    counter[item]+=1
    
while i< len(counter):
    while counter[i]==0:
        i+=1
    i+=5
    count+=1
    
print(count)
