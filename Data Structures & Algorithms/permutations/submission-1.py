class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]

        perms = self.permute(nums[1:])
        res = []

        for p in perms:
            for i in range(len(p)+1):
                p_copy = p.copy()
                p_copy.insert(i,nums[0])
                res.append(p_copy)
        return res


        # output = []

        # def rec(cur, left):
        #     if not left:
        #         output.append(cur[:])
        #         return

        #     for i in range(len(left)):
        #         cur.append(left[i])
        #         left.pop(i)          # remove by index
        #         rec(cur, left)
        #         left.insert(i, cur.pop())  # restore both cur and lef

        
        # rec([], nums)
        # return output