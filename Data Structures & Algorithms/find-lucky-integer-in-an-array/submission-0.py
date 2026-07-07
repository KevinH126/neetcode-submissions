class Solution:
    def findLucky(self, arr: List[int]) -> int:
        counts = Counter(arr)

        output = -1
        for k,v in counts.items():
            if v == k:
                output = max(output,v)
        return output