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
            if node not in visited and prereqMap[node] == []:
                output.append(node)
                visited.add(node)
                return True
            
            currVisited.add(node)
            allVisited = True
            for x in prereqMap[node]:
                if not dfs(x): return False
                if x not in visited:
                    allVisited = False
            if allVisited and node not in visited:
                prereqMap[node] = []
                output.append(node)
                visited.add(node)

            currVisited.remove(node)
            return True


        for i in range(numCourses):
            if not dfs(i): return []
        return output