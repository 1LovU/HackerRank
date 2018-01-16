# https://www.hackerrank.com/challenges/journey-to-the-moon/problem
# Learn disjoint set... BOOM
class DisjointSet(object):

    def __init__(self):
        self.leader = {} # maps a member to the group's leader
        self.group = {} # maps a group leader to the group (which is a set)

    def add(self, a, b):
        leadera = self.leader.get(a)
        leaderb = self.leader.get(b)
        if leadera is not None:
            if leaderb is not None:
                if leadera == leaderb: return # nothing to do
                groupa = self.group[leadera]
                groupb = self.group[leaderb]
                if len(groupa) < len(groupb):
                    a, leadera, groupa, b, leaderb, groupb = b, leaderb, groupb, a, leadera, groupa
                groupa |= groupb
                del self.group[leaderb]
                for k in groupb:
                    self.leader[k] = leadera
            else:
                self.group[leadera].add(b)
                self.leader[b] = leadera
        else:
            if leaderb is not None:
                self.group[leaderb].add(a)
                self.leader[a] = leaderb
            else:
                self.leader[a] = self.leader[b] = a
                self.group[a] = set([a, b])
               
           
       
n,m = map(int,input().split())
ds = DisjointSet()
nums = {i:'i' for i in range(n)}
for _ in range(m):
    u,v = map(int,input().split())
    nums.pop(u,None)
    nums.pop(v,None)    
    ds.add(u,v)
   

ds.group.update(nums)


size_of_all_values = [len(i) for i in ds.group.values()]

temp = 0
ans = 0
for item in size_of_all_values:
    ans += item * temp
    temp += item
print(ans)
    
