class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        visited = set()
        q = deque()
        components = 0
        for i in range(n):
            if i not in visited:
                components+=1
                q.append(i)
                while q:
                    cur = q.popleft()
                    for nei in adj[cur]:
                        if nei not in visited:
                            visited.add(nei)
                            q.append(nei)
        return components