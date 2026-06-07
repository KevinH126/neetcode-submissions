class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        s1char_counts = Counter(s1)
        s2char_counts = {}

        i = 0
        j = len(s1)-1
        while j < len(s2):
            s2char_counts = Counter(s2[i:j+1])
            if s1char_counts == s2char_counts:
                return True
            i+=1
            j+=1
        return False