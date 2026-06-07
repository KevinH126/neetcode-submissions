class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        subset = []
        def dfs(i):
            if i >= len(nums):
                res.append(subset[:])
                return

            subset.append(nums[i])
            dfs(i+1)

            subset.pop()
            dfs(i+1)

        dfs(0)
        return res
        
        
        
        # if not all(a <= b for a, b in pairwise(nums)):
        #     nums = sorted(nums)
        
        # output = []
        # def rec(curr):
        #     if len(curr) == len(nums):
        #         return curr
        #     for x in nums:
        #         if len(curr) == 0 or x > curr[-1]:
        #             curr.append(x)
        #             output.append(curr[:])
        #             rec(curr)
        #             curr.pop()
        # output.append([])
        # rec(output[-1])
        # return output

