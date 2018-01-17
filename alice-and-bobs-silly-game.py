# https://www.hackerrank.com/challenges/alice-and-bobs-silly-game/problem

import bisect

prime = []

for i in range(2, 100001):

    isprime = True
    maxval = int(i**0.5)
    isprime = True

    for itm in prime:
        if itm <= maxval:
            if i%itm == 0:
                isprime = False
                break
        else:
            break

    if isprime:
        prime.append(i)

g = int(input().strip())

for i in range(g):

    n = int(input().strip())
    moves = bisect.bisect(prime, n)
    moves += (moves < len(prime) and prime[moves] == n)
    print (('Bob', 'Alice')[moves%2])
