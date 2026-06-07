class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        def robber(houses):
            prev1 = houses[0]
            prev2 = 0
            for i in range(1, len(houses)):
                if prev2 + houses[i] > prev1:
                    temp = prev2
                    prev2 = prev1
                    prev1 = temp + houses[i]
                else:
                    prev2 = prev1
            return prev1
        output = max(robber(nums[:len(nums)-1]), robber(nums[1:]))
        return output