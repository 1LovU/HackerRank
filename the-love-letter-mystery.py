# https://www.hackerrank.com/challenges/the-love-letter-mystery/problem


T = int(input().strip())
for _ in range(T):    
    s = input().strip()
    sumChar = 0
    for i in range(0,len(s)):
        if i > len(s)-i-1 :
            break
        sumChar = sumChar + abs(ord(s[i])-ord(s[len(s)-i-1]))
    print(sumChar)
