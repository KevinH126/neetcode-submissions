class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ans = False

        def dfs(i, j, idx, curr):
            if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]) or board[i][j] != word[idx]:
                return False
            if board[i][j] == word[idx] and (i,j) not in curr:
                if idx == len(word)-1:
                    return True
                curr.add((i,j))
                ret = dfs(i+1, j, idx+1,curr) or dfs(i-1,j,idx+1,curr) or dfs(i,j+1,idx+1,curr) or dfs(i,j-1,idx+1,curr)
                curr.remove((i,j))
                return ret
            return False
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0] and dfs(i,j,0,set()):
                    return True
        return False
                    
            
            
            

