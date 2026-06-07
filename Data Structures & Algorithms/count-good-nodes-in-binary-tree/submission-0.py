# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.count = 0

        def dfs(curr, maxBefore):
            if not curr:
                return
            if curr.val >= maxBefore:
                self.count+=1
            maxB = max(maxBefore, curr.val)
            dfs(curr.left, maxB)
            dfs(curr.right, maxB)

        dfs(root, root.val)
        return self.count