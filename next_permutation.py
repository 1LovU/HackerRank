
# https://www.hackerrank.com/challenges/bigger-is-greater/problem
# Logic from :: https://www.nayuki.io/page/next-lexicographical-permutation-algorithm


def next_permutation(arr):
	# Find non-increasing suffix
	i = len(arr) - 1
	while i > 0 and arr[i - 1] >= arr[i]:
		i -= 1
	if i <= 0:
		return False
	
	# Find successor to pivot
	j = len(arr) - 1
	while arr[j] <= arr[i - 1]:
		j -= 1
	arr[i - 1], arr[j] = arr[j], arr[i - 1]
	
	# Reverse suffix
	arr[i : ] = arr[len(arr) - 1 : i - 1 : -1]
	return True



from copy import copy

for _ in range(int(input())):
    s1 = (input())
    s = list(s1)
    next_permutation(s)
    s = ''.join(s)
    if s1 == s:
        print('no answer')
       
    else:
        print(s)
    
    
           
        
        
