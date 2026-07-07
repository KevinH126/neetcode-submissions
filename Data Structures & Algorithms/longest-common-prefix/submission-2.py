class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        output = strs[0]

        for i in range(len(strs)-1):
            j = 1
            new = ""
            while j <= min(len(strs[i]), len(strs[i+1])) and strs[i][:j] == strs[i+1][:j]:
                new = strs[i][:j]
                j+=1
            if len(new) < len(output):
                output = new
        return output