class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        seen = set()
        minute = 0

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 2:
                    seen.add((i,j))
                    q.append((i,j,0))
        
        while q:
            i,j,m = q.popleft()
            minute = max(minute,m)
            if i-1 >=0 and grid[i-1][j] == 1 and (i-1,j) not in seen:
                seen.add((i-1,j))
                q.append((i-1,j,m+1))
            if i+1 < ROWS and grid[i+1][j] == 1 and (i+1,j) not in seen:
                seen.add((i+1,j))
                q.append((i+1,j,m+1))
            if j-1 >=0 and grid[i][j-1] == 1 and (i,j-1) not in seen:
                seen.add((i,j-1))
                q.append((i,j-1,m+1))
            if j+1 < COLS and grid[i][j+1] == 1 and (i,j+1) not in seen:
                seen.add((i,j+1))
                q.append((i,j+1,m+1))

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1 and (i,j) not in seen:
                    return -1

        return minute
            

