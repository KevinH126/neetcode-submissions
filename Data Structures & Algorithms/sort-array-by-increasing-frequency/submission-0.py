class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        counts = Counter(nums)

        buckets = [[] for i in range(len(nums)+1)]

        for k,v in counts.items():
            buckets[v].append(k)
        
        for i in range(len(buckets)):
            if len(buckets[i]) > 1:
                buckets[i].sort(reverse=True)
        output = []
        for i in range(1,len(buckets)):
            for x in buckets[i]:
                for j in range(i):
                    output.append(x)
        return output