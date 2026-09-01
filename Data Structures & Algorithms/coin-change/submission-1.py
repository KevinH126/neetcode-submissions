class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = {0:0} # amount : min number of coins
        
        def dfs(curAmount):
            if curAmount == 0:
                return 0
            if curAmount in dp:
                return dp[curAmount]
            
            minCoins = 999999
            for x in coins:
                if curAmount-x >= 0:
                    minCoins = min(minCoins, dfs(curAmount-x) + 1)
            dp[curAmount] = minCoins
            return dp[curAmount]


        dfs(amount)

        return -1 if dp[amount] >= 999999 else dp[amount]