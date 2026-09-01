class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereqMap = {x:[] for x in range(numCourses)}
        for a,b in prerequisites:
            prereqMap[a].append(b)
        
       # 3 -> 1,2 -> 0
       # 
        visited = set()
        currVisited = set()
        output = []
        def dfs(node):
            if node in currVisited:
                return False
            if node in visited:
                return True
            
            currVisited.add(node)
            for x in prereqMap[node]:
                if not dfs(x): return False
                

            currVisited.remove(node)
            output.append(node)
            visited.add(node)
            return True


        for i in range(numCourses):
            if not dfs(i): return []
        return output