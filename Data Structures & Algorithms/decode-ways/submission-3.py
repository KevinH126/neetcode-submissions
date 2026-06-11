class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [0] * len(s)
        def dfs(i):
            if i >= len(s):
                return 1
            if s[i] == "0":
                return 0
            if dp[i] > 0:
                return dp[i]
            dp[i] = dfs(i + 1)  # always try single digit
            if i + 2 <= len(s) and int(s[i:i+2]) <= 26:
                dp[i] += dfs(i + 2)  # also try two digits if valid
            return dp[i]  
        dfs(0)
        return dp[0]