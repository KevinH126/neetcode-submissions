class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        queue = deque()
        for i, x in enumerate(nums):
            while len(queue) > 0 and x > queue[-1]:
                queue.pop()
            queue.append(x)
            if i-k >= -1:
                if i-k >= 0 and nums[i-k] == queue[0]:
                    queue.popleft()
                res.append(queue[0])
        return res
                
            
            