class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        t_counts = Counter(t)
        total = len(t)
        res = ""
        best = len(s) + 1
        # OUZODYXAZV
        l, r = 0, 0
        while r < len(s):
            if s[r] in t:

                t_counts[s[r]] -= 1
                total -= 1 if t_counts[s[r]] >= 0 else 0
            while total == 0:
                if r-l+1 < best:
                    res = s[l:r+1]
                    best = len(res)
                if s[l] in t:
                    t_counts[s[l]] += 1
                    total += 1 if t_counts[s[l]] > 0 else 0
                l+=1
            r+=1
        return res
