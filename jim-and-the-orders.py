# https://www.hackerrank.com/challenges/jim-and-the-orders/problem

from collections import defaultdict
from sys import stdin

my_dict = defaultdict(list)
T = int(input())
for i in range(1,T+1):
    t,d = map(int,stdin.readline().split())
    my_dict[t+d].append(i)  

for key in sorted(my_dict):
    print(*my_dict[key],end=' ')






