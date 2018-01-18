# https://www.hackerrank.com/challenges/kangaroo/problem

x1,v1,x2,v2 = input().strip().split(' ')
x1,v1,x2,v2 = [int(x1),int(v1),int(x2),int(v2)]

if ((x2-x1) * (v1-v2)) > 0 and ((x2-x1)%(v1-v2))==0:
    print('YES')
else:
    print("NO")
