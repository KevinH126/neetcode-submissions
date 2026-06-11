class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0

        l,r = 0,0
        for i in range(len(s)):
            for j in range(2):    
                l=i
                r=i+j
                while l >= 0 and r < len(s) and s[l] == s[r]:
                    count+=1
                    l-=1
                    r+=1
        return count