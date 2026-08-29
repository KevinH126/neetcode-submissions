class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        output = []
        def dfs(i, curr):
            if i >= len(nums):
                output.append(curr[:])
                return
            
            curr.append(nums[i])
            dfs(i+1, curr)
            curr.pop()
            j = 1
            while i+j < len(nums) and nums[i+j] == nums[i]:
                j+=1
            dfs(i+j, curr)
        dfs(0,[])
        return output
