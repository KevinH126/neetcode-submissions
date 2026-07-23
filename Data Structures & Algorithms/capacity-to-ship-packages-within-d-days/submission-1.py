class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l,r = max(weights), sum(weights)

        res = r
        while l <= r:
            m = (l+r) // 2

            curr = 1
            i,j = 0,1
            total = weights[0]          # total == sum(weights[i:j])
            while j <= len(weights):
                if total > m:
                    curr += 1
                    i = j - 1
                    total = weights[i]
                j += 1
                if j <= len(weights):
                    total += weights[j-1]
            
            if curr > days:
                l = m + 1
            else:
                res = min(res,m)
                r = m - 1
        return res
