class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0] * (n+1)

        def rec(i):
            if i >= len(dp):
                return
            if i == 1:
                dp[i] = 1
            elif i == 2:
                dp[i] = 2
            else:
                dp[i] = dp[i-1] + dp[i-2]
            return rec(i+1)
        rec(1)
        return dp[n]

        