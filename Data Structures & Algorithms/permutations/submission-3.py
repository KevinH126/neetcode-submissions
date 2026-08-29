class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        output = []
        def dfs(curr,used):
            if len(curr) == len(nums):
                output.append(curr[:])
                return
            
            for j in range(len(nums)):
                if nums[j] not in used:
                    curr.append(nums[j])
                    used.add(nums[j])
                    dfs(curr,used)
                    used.remove(nums[j])
                    curr.pop()
                    
        dfs([],set())
        return output