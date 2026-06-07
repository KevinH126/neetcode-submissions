class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lower,upper = 1, max(piles) 

        result = 0
        while lower <= upper:
            k = (upper+lower)//2
            hour = 0
            for x in piles:
                hour += math.ceil(x/k)
            if hour > h:
                lower = k + 1
            if hour <= h:
                result = k
                upper = k-1
        return result


