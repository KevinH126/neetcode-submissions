class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        dp = {}

        def dfs(prev,i,j):
            if i < 0 or i >= ROWS or j < 0 or j >= COLS or prev >= matrix[i][j]:
                return 0
            if (i,j) in dp:
                return dp[(i,j)]
            dp[(i,j)] = max(dfs(matrix[i][j],i-1,j),dfs(matrix[i][j],i+1,j),dfs(matrix[i][j],i,j-1),dfs(matrix[i][j],i,j+1))+1
            return dp[(i,j)]
        
        res = 0
        for i in range(ROWS):
            for j in range(COLS):
                res = max(res,dfs(-1,i,j))
        return res
