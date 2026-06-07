class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        while n!=1:
            digits = [int(d) for d in str(n)]
            n = sum(d*d for d in digits)
            if n in seen:
                return False
            seen.add(n)
        return True
            
