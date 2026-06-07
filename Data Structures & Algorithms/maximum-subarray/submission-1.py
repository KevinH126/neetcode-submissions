class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        curr = nums[0] if nums[0] >= 0 else 0

        for i in range(1,len(nums)):
            curr+=nums[i]
            maxSum = max(curr,maxSum)
            if curr < 0:
                curr = 0
        return maxSum

