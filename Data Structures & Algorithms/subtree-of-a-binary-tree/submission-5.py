# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root, subRoot):
        if not subRoot: return True
        if not root: return False

        return self.sameTree(root,subRoot) or self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)

    def sameTree(self,r,s):
        if not r and not s:
            return True
        
        if r and s and r.val == s.val:
            return self.sameTree(r.left,s.left) and self.sameTree(r.right,s.right)
        return False