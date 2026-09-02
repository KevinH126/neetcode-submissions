class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = {}

        def dfs(i):
            if i in dp:
                return dp[i]

            longest = 1
            for j in range(i+1, len(nums)):
                if nums[i] < nums[j]:
                    longest = max(longest, 1+dfs(j))
            dp[i] = longest
            return dp[i]
        return max(dfs(i) for i in range(len(nums)))