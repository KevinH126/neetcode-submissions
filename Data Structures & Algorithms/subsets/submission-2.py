class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        output = []
        def rec(curr,i):
            if curr not in output:
                output.append(curr)
            if i >= len(nums):
                return
            rec(curr,i+1)
            rec(curr+[nums[i]],i+1)
        rec([],0)
        return output