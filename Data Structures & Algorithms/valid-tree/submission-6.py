class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) == 0:
            return True 
        if len(edges) != n-1:
            return False
        
        adj = collections.defaultdict(set)
        for x in edges:
            if x[0] == x[1]:
                return False
            adj[x[0]].add(x[1])
            adj[x[1]].add(x[0])
        
        q = deque([edges[0][0]])
        visit = set()
        f = 0
        while q:
            f+=1
            cur = q.popleft()
            visit.add(cur)
            for x in adj[cur]:
                if x not in visit:
                    q.append(x)
        return f==n