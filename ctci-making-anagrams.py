# https://www.hackerrank.com/challenges/ctci-making-anagrams/problem

from collections import Counter
def number_needed(a, b):
    ct_a = Counter(a)
    ct_b = Counter(b)
    ct_a.subtract(ct_b)
    return sum(map(abs,ct_a.values()))


a = input().strip()
b = input().strip()

print(number_needed(a, b))
