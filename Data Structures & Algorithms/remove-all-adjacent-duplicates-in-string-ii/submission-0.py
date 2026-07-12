class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []

        for i in range(len(s)):
            stack.append(s[i])
            while len(stack) >= k and len(set(stack[-k:])) <= 1:
                for i in range(k):
                    stack.pop()
        return "".join(stack)