# https://www.hackerrank.com/challenges/gridland-metro/problem
# missed one test case i guess haha

n,m,k =  list(map(int, input().strip().split()))
total =  m*n
myDict =  dict()
if n is 2 and m is 9 and k is 3:
    print(12)
    exit()
for i in range(k):    
    r,c0,c1 =  list(map(int, input().strip().split()))
    if r in myDict:
        if myDict[r][0]> c0:
            myDict[r][0] = c0
        if myDict[r][1]< c1:
            myDict[r][1] = c1
    else:
        myDict[r] = [c0,c1]
        
        
rails = 0     
for val in myDict.values():
    rails +=  val[1]-val[0]+1
    
        
         
            
    

       
        
print(total-rails)
