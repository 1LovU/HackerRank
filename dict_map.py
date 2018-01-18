# https://www.hackerrank.com/challenges/30-dictionaries-and-maps/problem

n =  int(input().strip())
myDict = dict()
for _ in range(n):
    s = input().strip().split()
    myDict[s[0]]=s[1]
while(True):
    try:
        i_key = input().strip()
    except:
        break
    if len(i_key) == 0 :
        break
    if i_key in myDict:
        print(i_key+'='+myDict[i_key])
    else:
        print('Not found')
