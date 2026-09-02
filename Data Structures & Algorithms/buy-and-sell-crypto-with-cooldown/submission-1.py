class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {} # (i,buy) : max profit when buying/selling at i

        def dfs(i,buy):
            if i >= len(prices):
                return 0
            if (i,buy) in dp:
                return dp[(i,buy)]
            
            if buy:
                dp[(i,buy)] = max(dfs(i+1,True), dfs(i+1,False) - prices[i])
            else:
                dp[(i,buy)] = max(dfs(i+1,False), prices[i] + dfs(i+2, True))
            return dp[(i,buy)]
        return dfs(0,True)
