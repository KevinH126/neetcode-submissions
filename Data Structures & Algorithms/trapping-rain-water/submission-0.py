class Solution:
    def trap(self, height: List[int]) -> int:
        i = 0
        j = len(height)-1
        level = 0
        max_level = max(height)-1
        area = 0
        while level <= max_level:
            while i < len(height) and height[i] <= level:
                i+=1
            while j >= 0 and height[j] <= level:
                j-=1
            if j-i >= 2:
                for k in range(i+1, j):
                    if height[k] <= level:
                        area+=1
            level+=1
        return area

