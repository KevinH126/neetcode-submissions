class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        output = []

        def rec(cur, left):
            if not left:
                output.append(cur[:])
                return

            for i in range(len(left)):
                cur.append(left[i])
                left.pop(i)          # remove by index
                rec(cur, left)
                left.insert(i, cur.pop())  # restore both cur and lef

        
        rec([], nums)
        return output