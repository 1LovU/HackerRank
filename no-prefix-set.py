# https://www.hackerrank.com/challenges/no-prefix-set

''' This is nice Trie Question, here is how you can do it.'''
from collections import Counter

def add_word(word):
    for i in range(0,len(word)+1):
        w = word[:i]
        count[w] += 1
        
     # Fist check is if the new word has a substring of previous words
     # second check is, if new word is a substring of previous words.
        if w in word_set or count[word] > 1:           
            return True
    word_set.add(word)       
    return False
        
T =  int(input())
count = Counter()
word_set = set()
flag = True
for _ in range(T):
    word = input().strip()    
    if add_word(word):
        print('BAD SET')
        print(word)
        flag = False
        break
if flag:
    print('GOOD SET')
