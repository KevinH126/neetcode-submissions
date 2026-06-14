class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        [1,2,4,6]
        #[1,1,2,8]
        #[48,24,12,8]

        fix = 1
        output = []
        for i in range(len(nums)):
            output.append(fix)
            fix = nums[i] * fix
        fix = 1
        for i in range(len(nums)-1,-1,-1):
            output[i] *= fix
            fix*= nums[i]
        return output