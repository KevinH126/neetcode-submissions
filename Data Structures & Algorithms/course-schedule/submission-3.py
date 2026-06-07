class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereqMap = {i:[] for i in range(numCourses)}
        for x in prerequisites:
            prereqMap[x[0]].append(x[1])

        visited = set()
        def dfs(crs):
            if crs in visited:
                return False
            if prereqMap[crs] == []:
                return True
            visited.add(crs)

            for pre in prereqMap[crs]:
                if not dfs(pre): return False
            visited.remove(crs)
            prereqMap[crs] = []
            return True
        
        for crs in range(numCourses):
            if not dfs(crs): return False
        return True



