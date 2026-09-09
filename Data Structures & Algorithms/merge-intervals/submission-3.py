class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key= lambda x: x[0])
        curr = intervals[0]
        res = []
        # [0,4] [1,4]

        for i in range(1,len(intervals)):
            if curr[1] < intervals[i][0]:
                res.append(curr)
                curr = intervals[i]
            elif curr[0] > intervals[i][1]:
                res.append(intervals[i])
            else:
                curr = [min(curr[0], intervals[i][0]), max(curr[1], intervals[i][1])]
        res.append(curr)
        return res