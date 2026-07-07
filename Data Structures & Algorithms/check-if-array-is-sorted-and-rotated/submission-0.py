class Solution:
    def check(self, nums: List[int]) -> bool:
        decreases = 0

        if nums[0] < nums[-1]:
            decreases=1
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                decreases+=1
            if decreases > 1:
                return False
        return True