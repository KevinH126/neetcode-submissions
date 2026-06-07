# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        self.isSame = True

        def dfs(a,b):
            if not a and not b:
                return
            if not a or not b:
                self.isSame = False
                return
            if a.val != b.val:
                self.isSame = False
            dfs(a.left,b.left)
            dfs(a.right, b.right)
        dfs(p,q)
        return self.isSame