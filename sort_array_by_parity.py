class Solution:
    """https://leetcode.com/problems/sort-array-by-parity/solution/"""
    def sortArrayByParity(self, A: 'List[int]') -> 'List[int]':
        odds, evens = [], []
        for i in A:
            if self.is_odd(i):
                odds.append(i)
            else:
                evens.append(i)
        A[:] = evens + odds
        return A

    @staticmethod
    def is_odd(num):
        return (num % 2)
