class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        curr = 1
        maxx = 1
        for i in range(len(nums)-1):
            if nums[i] < nums[i+1]:
                curr+=1
            else:
                maxx = max(maxx,curr)
                curr = 1
        maxx = max(maxx,curr)
        curr = 1
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                curr+=1
            else:
                maxx = max(maxx,curr)
                curr = 1
        maxx = max(maxx,curr)
        return maxx