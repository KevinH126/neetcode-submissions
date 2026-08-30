class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        maxArea = 0
        seen = set()


        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r,c) not in seen:
                    q.append((r,c))
                    seen.add((r,c))
                    currArea = 0
                    while q:
                        i,j = q.popleft()
                        
                        currArea+=1
                        if i-1 >= 0 and grid[i-1][j] == 1 and (i-1,j) not in seen: 
                            seen.add((i-1,j))
                            q.append((i-1,j))
                        if i+1 < ROWS and grid[i+1][j] == 1 and (i+1,j) not in seen: 
                            seen.add((i+1,j))
                            q.append((i+1,j))
                        if j-1 >= 0 and grid[i][j-1] == 1 and (i,j-1) not in seen: 
                            seen.add((i,j-1))
                            q.append((i,j-1))
                        if j+1 < COLS and grid[i][j+1] == 1 and (i,j+1) not in seen: 
                            seen.add((i,j+1))
                            q.append((i,j+1))
                    maxArea = max(maxArea,currArea)
        return maxArea