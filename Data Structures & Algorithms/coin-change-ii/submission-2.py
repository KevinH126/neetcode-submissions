class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        if amount == 0:
            return 1
        dp = {} # (amount,coin) : number of distinct combinations that total up to amount using coin

        def dfs(currAmount,i):
            if (currAmount,i) in dp:
                return dp[(currAmount,i)]
            if currAmount == 0:
                dp[(currAmount,i)] = 1
                return 1
            if currAmount < 0:
                return 0
            
            distinctWays = 0
            for j in range(i,len(coins)):
                distinctWays += dfs(currAmount-coins[j],j)
            dp[(currAmount,i)] = distinctWays
            return distinctWays
            
        output = 0
        for i in range(len(coins)):
            output += dfs(amount-coins[i], i)
        return output
