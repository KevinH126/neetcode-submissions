class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        output = []
        def dfs(i,curr):
            if i >= len(s):
                output.append(curr[:])
                return
            j = i
            while j < len(s):
                l,r = i, j
                pal = True
                while l<=r:
                    if s[l] != s[r]:
                        pal = False
                    l+=1
                    r-=1
                if pal:
                    curr.append(s[i:j+1])
                    dfs(j+1,curr)
                    curr.pop()
                
                j+=1
        dfs(0,[])
        return output
