class Solution:
    def reverseBits(self, n: int) -> int:
        output = 0

        i = 31
        while n > 0 and i >= 0:
            if n%2 == 1:
                output += 2 ** i
            n = n//2
            i-=1
        return output