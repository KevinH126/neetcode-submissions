class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        output = []
        nums.sort()
        def dfs(i, curr):
            total = sum(curr)
            if total == target:
                output.append(curr.copy())
                return
            for j in range(i, len(nums)):
                if total + nums[j] > target:
                    return
                curr.append(nums[j])
                dfs(j, curr)
                curr.pop()
        dfs(0,[])
        return output

