# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        output = []
        q = deque()
        if root:
            q.append((root,0))

        while q:
            curr,lvl = q.popleft()
            val = curr.val
            if len(output) < (lvl+1):
                output.append([val])
            else:
                output[lvl].append(val)
            if curr.left:
                q.append((curr.left,lvl+1))
            if curr.right:
                q.append((curr.right,lvl+1))
        return output
