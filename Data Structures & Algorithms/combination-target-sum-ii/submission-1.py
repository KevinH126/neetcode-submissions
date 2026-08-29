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

            if tuple(curr+[candidates[i]]) not in seen:
                curr.append(candidates[i])
                seen.add(tuple(curr))
                dfs(i+1, curr, total+candidates[i])
                curr.pop()
            dfs(i+1, curr, total)
            
        dfs(0, [], 0)
        return output