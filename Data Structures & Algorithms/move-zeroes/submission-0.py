class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        count = 0

        i,j = 0,0
        while i < len(nums) and j < len(nums):
            if nums[j] != 0:
                nums[i] = nums[j]
                i+=1
            else:
                count+=1
            j+=1
        
        for i in range(len(nums)-1, len(nums)-count-1, -1):
            nums[i] = 0
    
            