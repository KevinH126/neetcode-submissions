# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        output = []
        q = deque()
        q.append(root)
        output.append([root.val])
        while q:
            toadd = []
            vals = []
            while q:
                x = q.popleft()
                if x.left:
                    toadd.append(x.left)
                    vals.append(x.left.val)
                if x.right:
                    toadd.append(x.right)
                    vals.append(x.right.val)
            for x in toadd:
                q.append(x)
            if vals:
                output.append(vals)
        return output