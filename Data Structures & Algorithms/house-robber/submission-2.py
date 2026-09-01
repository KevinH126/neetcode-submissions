class Solution:
    def rob(self, nums: List[int]) -> int:
        # [1,1,3,3] rob(i) = max(nums[i] + rob(i-2), rob(i-1))
        rob = [0] * (len(nums)+2)

        for i in range(len(nums)):
            rob[i+2] = max(nums[i] + rob[i], rob[i+1])
        return rob[len(nums)+1]