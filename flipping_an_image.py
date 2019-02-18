class Solution:
    """https://leetcode.com/problems/flipping-an-image/solution/"""
    def flipAndInvertImage(self, A: 'List[List[int]]') -> 'List[List[int]]':
        for row in A:
            self.invert_color_and_flip_a_row(row)
        return A

    def invert_color_and_flip_a_row(self, row_matrix):
        row_matrix[:] = row_matrix[::-1]
        row_matrix[:] = [1 if i == 0 else 0 for i in row_matrix]