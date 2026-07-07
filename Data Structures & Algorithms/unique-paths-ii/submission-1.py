class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] == 1:
            return 0
        ROWS, COLS = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[-1]*COLS for i in range(ROWS)]

        def dfs(i,j):
            if i == ROWS-1 and j == COLS-1:
                return 1
            if dp[i][j] >= 0:
                return dp[i][j]
            
            total = 0
            if i+1 < ROWS and obstacleGrid[i+1][j] != 1:
                total += dfs(i+1,j)
            if j+1 < COLS and obstacleGrid[i][j+1] != 1:
                total += dfs(i,j+1)
            dp[i][j] = total
            return total
        return dfs(0,0)