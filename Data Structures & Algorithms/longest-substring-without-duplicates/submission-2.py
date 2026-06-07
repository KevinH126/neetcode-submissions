class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        maxL = 0

        l,r = 0,0
        while r < len(s):
            if s[r] in seen:
                if seen[s[r]] >= l:
                    l = seen[s[r]] + 1
            seen[s[r]] = r
            maxL = max(r-l+1, maxL)
            r+=1
        return maxL
