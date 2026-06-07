class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not all(a <= b for a, b in pairwise(nums)):
            nums = sorted(nums)
        
        output = []
        def rec(curr):
            if len(curr) == len(nums):
                return curr
            for x in nums:
                if len(curr) == 0 or x > curr[-1]:
                    curr.append(x)
                    output.append(curr[:])
                    rec(curr)
                    curr.pop()
        output.append([])
        rec(output[-1])
        return output

