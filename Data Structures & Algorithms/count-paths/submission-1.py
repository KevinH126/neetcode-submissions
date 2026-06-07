class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row = [1] * n

        for i in range(m-1):
            newRow = [1] * n
            for j in range(n-2, -1,-1):
                newRow[j] = newRow[j+1] + row[j]
            row = newRow
        return row[0]
        
        # dp = [[-1 for i in range(n)] for i in range(m)]

        # def dfs(x, y):
        #     if x == m-1 and y == n-1:
        #         return 1
        #     if dp[x][y] != -1:
        #         return dp[x][y]
        #     down, right = 0, 0
        #     if x+1 < m:
        #         down = dfs(x+1, y)
        #     if y+1 < n:
        #         right = dfs(x, y+1)
        #     dp[x][y] = down + right
        #     return dp[x][y]
        # return dfs(0,0)