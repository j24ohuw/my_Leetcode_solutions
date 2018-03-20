#https://www.hackerrank.com/challenges/ctci-making-anagrams/problem

def number_needed(a, b):
    intersection = set(a).intersection(b)
    dict_c = {char:min(a.count(char), b.count(char)) for char in intersection}
    return len(a) + len(b) - 2*sum(dict_c.values())
    
a = input().strip()
b = input().strip()

print(number_needed(a, b))
