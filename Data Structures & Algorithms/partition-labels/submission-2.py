class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastIndex = {} # char -> last index in s

        for i, c in enumerate(s):
            lastIndex[c] = i

        res = []
        size, end = 0,0
        for i, c in enumerate(s):
            size+=1
            end = max(end, lastIndex[c])

            if i == end:
                res.append(size)
                size = 0
        return res
        # stack = []
        # chars = {}

        # for i in range(len(s)):
        #     if s[i] not in chars:
        #         stack.append(i)
        #         chars[s[i]] = i
        #     else:
        #         while stack[-1] > chars[s[i]]:
        #             stack.pop()
        
        # output = []
        # for i in range(len(stack)-1):
        #     output.append(stack[i+1] - stack[i])
        # output.append(len(s)-stack[-1])
        # return output