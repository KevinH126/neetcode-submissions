class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        output = []
        def dfs(curr,openN, closedN):
            if openN == closedN == n:
                output.append(curr)
                return
            
            if openN < n:
                dfs(curr+"(",openN+1,closedN)
            if openN > closedN:
                dfs(curr+")", openN, closedN+1)
        dfs("",0,0)
        return output
            

            
