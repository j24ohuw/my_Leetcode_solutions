#https://www.hackerrank.com/challenges/ctci-comparator-sorting/problem

from functools import cmp_to_key
class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def __repr__(self):
        pass
    def comparator(a, b):
        if a.score < b.score: return 1
        if a.score > b.score: return -1
        if a.name.lower() > b.name.lower(): return 1
        if a.name.lower() < b.name.lower(): return -1
        return 0
        
