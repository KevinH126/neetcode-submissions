class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trustedby_counts = {}
        trusts_counts = {}
        for i in range(1,n+1):
            trustedby_counts[i] = 0
            trusts_counts[i] = 0

        for x in trust:
            trusts_counts[x[0]] +=1 
            trustedby_counts[x[1]] +=1
        
        for k,v in trustedby_counts.items():
            if v == n-1 and trusts_counts[k] == 0:
                return k
        return -1