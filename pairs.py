# https://www.hackerrank.com/challenges/pairs

#!/usr/bin/py
# Head ends here
def pairs(a,k):
    # a is the list of numbers and k is the difference value
    a = set(a)
    

    answer = 0
    for item in a:
        if item+k in a :
            answer+=1
    return answer
# Tail starts here
if __name__ == '__main__':
    a = input().strip()
    a = list(map(int, a.split(' ')))
    _a_size=a[0]
    _k=a[1]
    b = input().strip()
    b = list(map(int, b.split(' ')))
    print(pairs(b,_k))
