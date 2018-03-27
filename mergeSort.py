#!/bin/python3
#https://www.hackerrank.com/challenges/ctci-merge-sort/problem

import sys

def merge_sort(arr):
    middle = len(arr)//2
    if middle == 0: return arr, 0
    
    arr_left, a = merge_sort(arr[:middle]) 
    arr_right, b = merge_sort(arr[middle:])
    arr,c = merge(arr_left, arr_right)
    return arr, a+b+c

def merge(left, right):
    inversions = 0 
    temp = []
    L = 0
    R = 0
    while len(left) > L and len(right) > R:
        num_left = left[L]
        num_right = right[R]
        if  num_left > num_right:
            R += 1
            temp.append(num_right)
            inversions += len(left) - L
        else:
            L += 1
            temp.append(num_left)
    return temp + left[L:] + right[R:], inversions

def countInversions(arr):
    # Complete this function
    _, count = merge_sort(arr)
    return count
    
if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        n = int(input().strip())
        arr = list(map(int, input().strip().split(' ')))
        result = countInversions(arr)
        print(result)
