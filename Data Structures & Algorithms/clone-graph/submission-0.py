"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        oldToNew = {None: None}
        q = deque()
        if node:
            q.append(node)

        while q:
            curr = q.popleft()
            neighbors = []
            if curr not in oldToNew:
                oldToNew[curr] = Node(curr.val)
            for x in curr.neighbors:
                if x not in oldToNew:
                    oldToNew[x] = Node(x.val)
                    q.append(x)
                neighbors.append(oldToNew[x])
            oldToNew[curr].neighbors = neighbors
        return oldToNew[node]

