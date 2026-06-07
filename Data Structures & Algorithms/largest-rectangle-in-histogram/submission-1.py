class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        if not heights: return 0
        stack = [(0,heights[0])]
        maxArea = 0

        for i in range(1,len(heights)):
            curr = i
            while stack and heights[i] < stack[-1][1]:
                area = (i-stack[-1][0])*stack[-1][1]
                maxArea = max(maxArea, area)
                curr = stack[-1][0]
                stack.pop()
            stack.append((curr,heights[i]))
        i=len(heights)
        while stack:
            area = (i-stack[-1][0])*stack[-1][1]
            maxArea = max(maxArea, area)
            stack.pop()
        return maxArea