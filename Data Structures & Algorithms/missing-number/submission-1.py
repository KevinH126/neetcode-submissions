class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        summ = 0
        for i in range(0,len(nums)+1):
            summ+=i
        
        curr = 0
        for x in nums:
            curr+=x
        
        return summ-curr


