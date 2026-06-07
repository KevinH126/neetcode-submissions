class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0] * (len(nums)+2)
        currMax = 0

        for i in range(2, len(dp)):
            currMax = max(dp[i-2], currMax)
            dp[i] = currMax + nums[i-2]
        return max(dp[-1], dp[-2])