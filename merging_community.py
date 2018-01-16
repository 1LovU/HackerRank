# https://www.hackerrank.com/challenges/merging-communities/problem
# its all about disjoint set. 

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

                
ds = DisjointSet()
N,Q = map(int,input().split())
for _ in range(Q):
    s = input().split()
    if s[0] is 'Q':
        flag = False
        if len(ds.group.items()) == 0:
            ds.add(s[1],s[1])                    
            print(len(ds.group[s[1]]))
            flag = True
           
        else:
            key = ds.leader.get(s[1],False)
            if key:
                val = ds.group[key]
                print(len(val))
                flag = True              
               
           
        if not flag:
            ds.add(s[1],s[1])
            print(len(ds.group[s[1]]))
            
 
    else:
        ds.add(s[1],s[2])
