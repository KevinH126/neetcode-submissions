class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        output = []
        curr = []
        def dfs(i):
            if sum(curr) == target:
                output.append(curr[:])
                return
            if i >= len(nums) or sum(curr) > target:
                return
            
            for j in range(i, len(nums)):
                curr.append(nums[j])
                dfs(j)
                curr.pop()
        dfs(0)
        return output