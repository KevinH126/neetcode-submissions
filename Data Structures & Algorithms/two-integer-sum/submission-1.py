class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapp = {}

        for i in range(len(nums)):
            tt = target - nums[i]
            if tt in mapp:
                return [mapp[tt],i]
            mapp[nums[i]] = i