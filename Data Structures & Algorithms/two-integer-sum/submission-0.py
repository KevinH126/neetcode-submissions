class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapp = {}

        for i in range(len(nums)):
            t = target - nums[i]
            if t in mapp:
                return [mapp[t],i]
            else:
                mapp[nums[i]] = i