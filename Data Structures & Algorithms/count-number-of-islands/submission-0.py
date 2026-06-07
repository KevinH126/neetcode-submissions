class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        num = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    q.append((r,c))
                    
                    while q:
                        i,j = q.popleft()
                        grid[i][j] = "0"
                        if i-1 >= 0 and grid[i-1][j] == "1": q.append((i-1,j))
                        if i+1 < ROWS and grid[i+1][j] == "1": q.append((i+1,j))
                        if j-1 >= 0 and grid[i][j-1] == "1": q.append((i,j-1))
                        if j+1 < COLS and grid[i][j+1] == "1": q.append((i,j+1))
                    num+=1
        return num