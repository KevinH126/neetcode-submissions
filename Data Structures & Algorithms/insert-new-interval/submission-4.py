class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if len(intervals) == 0:
            return [newInterval]
        insIdx = len(intervals)
        for i in range(len(intervals)):
            if newInterval[0] < intervals[i][0]:
                insIdx = i
                break
        while insIdx < len(intervals) and newInterval[1] >= intervals[insIdx][1]:
            intervals.pop(insIdx)
        
        if insIdx > 0:
            if newInterval[0] <= intervals[insIdx-1][1]:
                newInterval = [intervals[insIdx-1][0], max(newInterval[1],intervals[insIdx-1][1])]
                intervals.pop(insIdx-1)
                insIdx -=1
        if insIdx < len(intervals):
            if newInterval[1] >= intervals[insIdx][0]:
                newInterval = [newInterval[0], intervals[insIdx][1]]
                intervals.pop(insIdx)
        intervals.insert(insIdx,newInterval)
        return intervals
