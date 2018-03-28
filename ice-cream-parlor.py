#https://www.hackerrank.com/challenges/ctci-ice-cream-parlor/problem

#!/bin/python3

import sys

def solve(arr, money):
    # Complete this function
    table = {}
    for id, cost in enumerate(arr):
        if table.get(cost,0) == 0:
            if table.get(money-cost,0) > 0:
                print(table[money-cost], id+1)
            table[cost] = id+1
        else:
            if table.get(money-cost,0) > 0:
                print(table[cost], id+1)
    return False
    
if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        money = int(input().strip())
        n = int(input().strip())
        arr = list(map(int, input().strip().split(' ')))
        solve(arr, money)
