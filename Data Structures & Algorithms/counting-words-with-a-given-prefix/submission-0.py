class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        count = 0

        for x in words:
            if x[:len(pref)] == pref:
                count+=1
        return count