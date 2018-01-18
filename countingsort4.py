# https://www.hackerrank.com/challenges/countingsort4/problem

""" How about Using a Defaultdict?  I am not sure if its a right thing   for Counter sort, but I use it almost everytime :)
"""

from sys import stdin, stdout
from collections import defaultdict

T = int(stdin.readline())
count_dict = defaultdict(list)
max_index = 0
for i in range(T):
    index, value = stdin.readline().split()
    index = int(index)
    if i < T//2:
        count_dict[index].append('-')
    else:
        count_dict[index].append(value)       
    max_index = max(max_index, index)

for index in range(max_index+1):
    value = count_dict[index]    
    print(*value, end=' ')
