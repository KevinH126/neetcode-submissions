class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        #   c a t
        # c 3 2 1
        # r 2 2 1
        # a 2 2 1
        # b 1 1 1
        # t 1 1 1

        dp = [[0] * (len(text2)+1) for i in range(len(text1)+1)]

        for i in range(len(text1)-1, -1,-1):
            for j in range(len(text2)-1, -1, -1):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i+1][j+1]
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j+1])
        return dp[0][0]