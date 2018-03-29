#https://www.hackerrank.com/challenges/ctci-recursive-staircase/problem

p = {0:0,
    1:1,
    2:2,
    3:4}

def permutations(n,p):
    if p.get(n,0) == 0 and n > 3:
        combination =  permutations(n-3,p) + permutations(n-2,p) + permutations(n-1,p)
        p[n] = combination
        return combination
    else:
        return p.get(n)
        
s = int(input().strip())
for a0 in range(s):
    n = int(input().strip())
    print(permutations(n,p))
