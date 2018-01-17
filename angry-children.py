# https://www.hackerrank.com/challenges/angry-children/problem



t = int(input().strip())
k= int(input().strip())
nums = []
for i in range(t):
    nums.append(int(input().strip()))
nums.sort()
for i in range(k,t+1):
    diff = nums[i-1]-nums[i-k]    
    if i==k:
        minDiff = diff
    elif minDiff > diff:
        minDiff = diff
print(minDiff)
