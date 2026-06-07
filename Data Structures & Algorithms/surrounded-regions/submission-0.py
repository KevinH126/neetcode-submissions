class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        seen = set()

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'O' and (r,c) not in seen:
                    valid = True
                    q = deque()
                    q.append((r,c))
                    curr = set()
                    while q:
                        i,j = q.popleft()
                        curr.add((i,j))
                        seen.add((i,j))

                        if i-1 < 0 or i+1 >= ROWS or j-1 < 0 or j+1 >= COLS:
                            valid = False
                        if i-1 >= 0 and board[i-1][j] == 'O' and (i-1,j) not in seen:
                            q.append((i-1,j))
                        if i+1 < ROWS and board[i+1][j] == 'O' and (i+1,j) not in seen:
                            q.append((i+1,j))
                        if j-1 >= 0 and board[i][j-1] == 'O' and (i,j-1) not in seen:
                            q.append((i,j-1))
                        if j+1 < COLS and board[i][j+1] == 'O' and (i,j+1) not in seen:
                            q.append((i,j+1))
                    if valid:
                        while curr:
                            i,j = curr.pop()
                            board[i][j] = 'X'

