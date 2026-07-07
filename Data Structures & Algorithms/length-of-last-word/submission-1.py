class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count = 0
        f = False
        for i in range(len(s)-1,-1,-1):
            if f== True and s[i] == " ":
                return count
            if s[i] != " ":
                f = True
                count +=1
        return count