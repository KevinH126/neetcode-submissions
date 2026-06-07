class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        stack = []
        chars = {}

        for i in range(len(s)):
            if s[i] not in chars:
                stack.append(i)
                chars[s[i]] = i
            else:
                while stack[-1] > chars[s[i]]:
                    stack.pop()
        
        output = []
        for i in range(len(stack)-1):
            output.append(stack[i+1] - stack[i])
        output.append(len(s)-stack[-1])
        return output