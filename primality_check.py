#https://www.hackerrank.com/challenges/ctci-big-o/problem


def is_prime(n):
    if n == 2: return True
    if n <= 1: return False
    prime = {}
    high = int(n**0.5)
    for i in range(2,high+1):
        if n % i == 0:
            return False
    return True
            

p = int(input().strip())
for a0 in range(p):
    n = int(input().strip())
    if is_prime(n): print('Prime')
    else:           print('Not prime')
    
