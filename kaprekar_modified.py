# https://www.hackerrank.com/challenges/kaprekar-numbers/problem


def kepler(m,n):  
       
    if m ==1  and n>=9:
        keps= [1,9]  
        m = 10
    else:
        keps = []
    for i in range(m,n+1):
        sq = str(i**2)
        mid = len(sq)//2        
        p = sq[:mid]
        q = sq[mid:]
        
        
        if int(p)+int(q) == i:            
            keps.append(i)
           
       
    return keps
   

if __name__ == '__main__':
    m = int(input())
    n =  int(input())
    
    keps = kepler(m,n)
    if len(keps) == 0:
        print('INVALID RANGE')
       
    else:
        print(*keps)
