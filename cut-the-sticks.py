# https://www.hackerrank.com/challenges/cut-the-sticks/problem

n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
while arr:
    print(len(arr))
    arr = [x for x in arr if x != min(arr)] 
    
