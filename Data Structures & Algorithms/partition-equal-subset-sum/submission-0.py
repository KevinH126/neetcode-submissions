class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False
        
        subsetSum = sum(nums)//2
        dp = {} # (i,sum) : 

        def dfs(i,currSum):
            if currSum == subsetSum:
                return True
            if i >= len(nums):
                return False
            if (i,currSum) in dp:
                return dp[(i,currSum)]
            
            dp[(i,currSum)] = dfs(i+1,currSum) or dfs(i+1,currSum+nums[i])
            return dp[(i,currSum)]
        
        return dfs(0,0)
