# https://www.hackerrank.com/challenges/counter-game


t = int(input().strip())
for _ in range(t):
    num =  int(input().strip())
    num -= 1
    binNum = str((bin(num)[2:]))
    counter  =  binNum.count('1')
    if counter % 2 == 0:
        print('Richard')
    else:
        print('Louise')
        
    
