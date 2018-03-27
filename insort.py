#https://www.hackerrank.com/challenges/ctci-find-the-running-median/problem

#!/bin/python3

import sys
import bisect


def bin_search(arr, val):
    low = 0
    high = len(arr)
    while low < high:
        mid = (high + low)//2
        if val < arr[mid]:
            high = mid
        else:
            low = mid + 1
    return low

n = int(input().strip())
a = []
a_i = 0
for a_i in range(n):
    a_t = int(input().strip())
    a.append(a_t)

arr = []
for i in a:
    pos = bin_search(arr,i)
    arr.insert(pos, i)
    if len(arr) % 2 == 0:
        mid_left = len(arr)/2 -1
        mid_right = len(arr)/2
        print(float(arr[int(mid_left)] + arr[int(mid_right)])/2)
    else:
        print(float(arr[int(len(arr)/2)]))
        
        

        
        
        
        
        
        
        
        
