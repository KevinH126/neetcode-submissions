class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        if len(t) == len(s) and s == t:
            return s
        minWindow = ""
        
        tFreq = Counter(t)
        currFreq = {ch:0 for ch in t}

        i = 0
        
        j = i
        have,need = 0, len(tFreq)
        while j < len(s):
            if s[j] in currFreq:
                currFreq[s[j]]+=1
                if currFreq[s[j]] == tFreq[s[j]]:
                    have+=1
                while have == need:
                    minWindow = s[i:j+1] if len(minWindow) == 0 or len(minWindow) > len(s[i:j+1]) else minWindow
                    if s[i] in currFreq:
                        currFreq[s[i]]-=1
                        if currFreq[s[i]] < tFreq[s[i]]:
                            have-=1
                            i+=1
                            break
                    i+=1
            j+=1
        return minWindow
        