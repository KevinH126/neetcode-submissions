class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        dp = [[0] * cols for _ in range(rows)]

        def dfs(i,j):
            if dp[i][j] > 0:
                return dp[i][j]
            
            f = 0
            if i-1 >= 0 and matrix[i][j] < matrix[i-1][j]:
                f = max(f, dfs(i-1,j))
            if i+1 < rows and matrix[i][j] < matrix[i+1][j]:
                f = max(f, dfs(i+1,j))
            if j-1 >= 0 and matrix[i][j] < matrix[i][j-1]:
                f = max(f, dfs(i,j-1))
            if j+1 < cols and matrix[i][j] < matrix[i][j+1]:
                f = max(f, dfs(i,j+1))
            dp[i][j] = f+1
            return f+1


        output = -1
        for r in range(rows):
            for c in range(cols):
                output = max(output, dfs(r,c))
        return output