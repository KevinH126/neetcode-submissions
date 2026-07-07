class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        evens = []
        odds = []

        for x in nums:
            if x > 0:
                evens.append(x)
            elif x < 0:
                odds.append(x)

        output = []
        for i in range(len(nums)):
            if i % 2 == 0:
                output.append(evens[i//2])
            else:
                output.append(odds[i//2])
        return output