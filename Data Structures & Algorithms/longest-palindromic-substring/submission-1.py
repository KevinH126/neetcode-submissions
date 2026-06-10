class Solution:
    def longestPalindrome(self, s: str) -> str:
        curr = ""

        l,r = 0,0
        for i in range(len(s)):
            for j in range(0,2):
                l = i
                r = i+j
                while l >= 0 and r < len(s) and s[l] == s[r]:
                    if len(curr) < (r-l+1):
                        curr = s[l:r+1]
                    l-=1
                    r+=1
        return curr