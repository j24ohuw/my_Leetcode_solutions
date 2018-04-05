#https://www.hackerrank.com/challenges/ctci-making-anagrams/problem

def number_needed(a, b):
    set_a = build_set(a)
    set_b = build_set(b)
    intersection = ''
    
    for key,val in set_a.items():
        if set_b.get(key,0) != 0:
            min_val = min(val,set_b[key])
            intersection += key*min_val
    return len(a)+len(b) - 2*len(intersection) 
    
    
def build_set(a):
    set_a = {}
    for i in a:
        if set_a.get(i,0) == 0:
            set_a[i] = 1
        else:
            set_a[i] += 1
    return set_a
