class Solution:
    """Solution for https://leetcode.com/problems/n-repeated-element-in-size-2n-array/submissions/"""
    def repeatedNTimes(self, A: 'List[int]') -> 'int':
        char_to_count_map = dict()
        for char in A:
            if char in char_to_count_map:
                return char
            else:
                char_to_count_map[char] = 1
