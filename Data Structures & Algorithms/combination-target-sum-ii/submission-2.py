class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        output = []
        seen = set()
        def dfs(i, curr, total):
            if total == target:
                output.append(curr[:])
                return
            
            if i >= len(candidates) or total > target:
                return
            curr.append(candidates[i])
            dfs(i+1, curr, total+candidates[i])
            curr.pop()
            j = 1
            while i+j < len(candidates) and candidates[i+j] == candidates[i]:
                j+=1
            dfs(i+j, curr, total)
            
        dfs(0, [], 0)
        return output