# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validbst(curr, low=float('-inf'), high=float('inf')):
            if not curr:
                return True
            if curr.val <= low or curr.val >= high:
                return False
            
            return validbst(curr.left, low, curr.val) and validbst(curr.right, curr.val, high)
        return validbst(root)
#   5
# 4   6
#    3 7
#