# https://www.hackerrank.com/challenges/string-reduction/problem

#!/usr/bin/py
# Head ends here

def stringReduction(a):
    count_a = a.count('a')
    count_b = a.count('b')
    count_c = a.count('c')
    rem_a = count_a % 2
    rem_b = count_b % 2
    rem_c = count_c % 2
    if (count_a == 0 and count_b==0) or (count_c == 0 and count_b==0) or (count_a == 0 and count_c==0):
        return len(a) 
    elif (rem_a==0 and rem_b==0 and rem_c==0) or (rem_a==1 and rem_b==1 and rem_c==1):
        return 2
    else:
        return 1
# Tail starts here
if __name__ == '__main__':
    t = int(input())
    for i in range(0,t):
        a=input()
        print(stringReduction(a))
