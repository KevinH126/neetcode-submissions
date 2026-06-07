# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = [root]
        seen = set()

        while k > 0:
            curr = stack[-1]
            if curr.left and curr.left not in seen:
                stack.append(curr.left)
            else: 
                if curr not in seen: 
                    k-=1
                    seen.add(curr)
                if k == 0:
                    return curr.val
                elif curr.right and curr.right not in seen:
                    stack.append(curr.right)
                else:
                    seen.add(curr)
                    stack.pop()

                
        return stack[-1].val
                