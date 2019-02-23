# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    """https://leetcode.com/problems/search-in-a-binary-search-tree/submissions/"""
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if root is None:
            return None
        elif root.val < val:
            return self.searchBST(root.right, val)
        elif root.val > val:
            return self.searchBST(root.left, val)
        return root
