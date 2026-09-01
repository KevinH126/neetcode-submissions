class Solution:
    def numDecodings(self, s: str) -> int:
        # 1112
        # dp[i] = number of ways to encode from i to end

        # dp[3] = dp[4] + 1 + 0= 0 + 1 = 1
        # dp[2] = dp[3] + 1 + dp[4] + 1

        dp = {len(s) : 1}

        for i in range(len(s)-1, -1, -1):
            if '1' <= s[i] <= '9':
                dp[i] = dp[i+1]
            else:
                dp[i] = 0

            if i < len(s)-1 and (
                (s[i] == '1' and '0' <= s[i+1] <= '9') or
                (s[i] == '2' and '0' <= s[i+1] <= '6')
            ):
                dp[i] += dp[i+2]

        return dp[0]