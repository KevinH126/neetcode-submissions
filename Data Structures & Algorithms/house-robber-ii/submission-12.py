class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(self.houseRobber(nums[1:]), self.houseRobber(nums[:-1]), nums[0])
        
    def houseRobber(self, nums):
        rob1, rob2 = 0, 0

        for x in nums:
            temp = max(rob1 + x, rob2)
            rob1 = rob2
            rob2 = temp
        return max(rob1, rob2)