# https://www.hackerrank.com/challenges/py-collections-ordereddict/problem

from collections import OrderedDict

Order_Dict = OrderedDict()

for _ in  range(int(input())):
    Query =  input().strip().split()
    price = int(Query[-1])
    del Query[-1]
    item = ' '.join(Query)
    if item not in Order_Dict:
        Order_Dict[item] = price
       
    else:
        Order_Dict[item] += price

for key,val in Order_Dict.items():
    print(key,val)
    
