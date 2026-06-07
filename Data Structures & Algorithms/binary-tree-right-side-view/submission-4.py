# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        output = []

        def dfs(curr, height):
            if not curr:
                return
            
            if len(output) == height:
                output.append(curr.val)
            dfs(curr.right,height+1)
            dfs(curr.left,height+1)
        dfs(root, 0)
        return output

