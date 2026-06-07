# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validBST(curr, low=float('-inf'), high=float('inf')):
            if not curr:
                return True
            if curr.val >= high or curr.val <= low:
                return False
            
            return validBST(curr.left, low, curr.val) and validBST(curr.right, curr.val, high)
        
        return validBST(root)


#   5
# 4   6
#    3 7
#