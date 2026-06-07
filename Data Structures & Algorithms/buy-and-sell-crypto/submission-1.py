class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        profit = 0

        i,j = 0,1
        while j < len(prices):
            curr = prices[j]-prices[i]
            if curr < 0:
                curr = 0
            profit = max(profit, curr)
            if prices[j] < prices[i]:
                i = j
            j+=1
        return profit
            
            