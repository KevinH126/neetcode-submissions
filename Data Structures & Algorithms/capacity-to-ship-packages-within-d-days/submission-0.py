class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l,r = max(weights), sum(weights)

        res = r
        while l <= r:
            m = (l+r) // 2

            curr = 1
            i,j = 0,1
            while j <= len(weights):
                if sum(weights[i:j]) <= m:
                    j+=1
                else:
                    curr+=1
                    i = j-1
                    j+=1
            
            if curr > days:
                l = m + 1
            else:
                res = min(res,m)
                r = m - 1
        return res
