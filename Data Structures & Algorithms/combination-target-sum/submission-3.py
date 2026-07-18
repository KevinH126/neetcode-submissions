class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        output = []
        nums.sort()
        def dfs(i, curr):
            total = sum(curr)
            if total == target:
                output.append(curr.copy())
                return
            if i >= len(nums) or total > target:
                return
            
            curr.append(nums[i])
            dfs(i, curr)
            curr.pop()
            dfs(i+1, curr)
        dfs(0,[])
        return output

