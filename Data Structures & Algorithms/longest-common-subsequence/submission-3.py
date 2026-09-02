class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        #   c a t
        # c 3 2 1
        # r 2 2 1
        # a 2 2 1
        # b 1 1 1
        # t 1 1 1

        dp = {} # (i,j) : LCS from text1[i:] and text2[j:]

        def dfs(i,j):
            if i >= len(text1) or j >= len(text2):
                return 0
            if (i,j) in dp:
                return dp[(i,j)]

            if text1[i] == text2[j]:
                dp[(i,j)] = 1+dfs(i+1,j+1)
            else:
                dp[(i,j)] = max(dfs(i+1,j),dfs(i,j+1))
            return dp[(i,j)]
        return dfs(0,0)


