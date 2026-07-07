class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums = sorted(nums)

        
        l,r = 1, len(nums)
        i = 0
        while l <= r:
            i=0
            mid = (l+r)//2
            while i < len(nums) and nums[i] < mid:
                i+=1
            if len(nums) - i == mid:
                return mid
            elif len(nums) - i > mid:
                l = mid+1
            else:
                r = mid-1
        return -1
