# https://www.hackerrank.com/challenges/maximizing-xor/problem


#!/usr/bin/python3
def maxXor(l, r):
    max_value = 0
    for i in range(l,r+1):
        for j in range(l+1,r+1):
            if i^j > max_value:
                max_value = i^j
    return max_value
         
if __name__ == '__main__':
  l = int(input())
  r = int(input())
  print(maxXor(l, r))
