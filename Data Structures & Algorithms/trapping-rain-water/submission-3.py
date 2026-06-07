class Solution:
    def trap(self, height: List[int]) -> int:

        if not height: return 0
        result = 0
        maxL,maxR = height[0],height[-1]

        l,r = 0, len(height)-1

        while l < r:
            if maxL <= maxR:
                l+=1
                w = min(maxL,maxR) - height[l]
                if w > 0:
                    result+=w
                maxL = max(maxL,height[l])
            else:
                r-=1
                w = min(maxL,maxR) - height[r]
                if w > 0:
                    result+=w
                maxR = max(maxR, height[r])
        return result